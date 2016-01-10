import sys
import os
import json
from resources.lib.config import cConfig
from resources.lib import common, logger
from resources.lib.handler.requestHandler import cRequestHandler
from distutils.version import LooseVersion

class cPluginHandler:

    def __init__(self):
        self.addon = common.addon
        self.rootFolder = common.addonPath
        self.settingsFile = os.path.join(self.rootFolder, 'resources', 'settings.xml')
        self.profilePath = common.profilePath
        self.pluginDBFile = os.path.join(self.profilePath,'pluginDB')
        logger.info('profile folder: %s' % self.profilePath)
        logger.info('root folder: %s' % self.rootFolder)
        self.defaultFolder =  os.path.join(self.rootFolder, 'sites')
        logger.info('default sites folder: %s' % self.defaultFolder)
        self.checkForSiteUpdates()

    def getAvailablePlugins(self):
        pluginDB = self.__getPluginDB()
        # default plugins
        update = False
        fileNames = self.__getFileNamesFromFolder(self.defaultFolder)
        for fileName in fileNames:
            plugin = {'name':'', 'icon':'', 'settings':'', 'modified':0}
            if fileName in pluginDB:
                plugin.update(pluginDB[fileName])
            try:
                modTime = os.path.getmtime(os.path.join(self.defaultFolder,fileName+'.py'))
            except OSError:
                modTime = 0
            if fileName not in pluginDB or modTime > plugin['modified']:
                logger.info('load plugin: ' + str(fileName))
                # try to import plugin
                pluginData = self.__getPluginData(fileName)
                if pluginData:
                    pluginData['modified'] = modTime
                    pluginDB[fileName] = pluginData
                    update = True
        # check pluginDB for obsolete entries
        deletions = []
        for pluginID in pluginDB:
            if pluginID not in fileNames:
                deletions.append(pluginID)
        for id in deletions:
            del pluginDB[id]
        if update or deletions:
            self.__updateSettings(pluginDB)
            self.__updatePluginDB(pluginDB)
        return self.getAvailablePluginsFromDB()

    def getAvailablePluginsFromDB(self):
        plugins = []
        oConfig = cConfig()
        iconFolder = os.path.join(self.rootFolder, 'resources','art','sites')
        pluginDB = self.__getPluginDB()
        for pluginID in pluginDB:
            plugin = pluginDB[pluginID]
            pluginSettingsName = 'plugin_%s' % pluginID
            plugin['id'] = pluginID
            if 'icon' in plugin:
                plugin['icon'] = os.path.join(iconFolder, plugin['icon'])
            else:
                plugin['icon'] = ''
            # existieren zu diesem plugin die an/aus settings
            if oConfig.getSetting(pluginSettingsName) == 'true':
                plugins.append(plugin)
        return plugins

    def get_settings(self, oSettingsHandler):
        aPlugins = []
        aPlugins = self.getAvailablePlugins()

        oSettingsHandler.addCategory('30022', 'site_settings')

        for pluginEntry in aPlugins:
            oSettingsHandler.addBool('site_settings', pluginEntry['id'], pluginEntry['name'], 'false')
            try:
                plugin = __import__(pluginEntry['id'], globals(), locals())
                function = getattr(plugin, 'get_settings')
                oSettingsHandler = function(oSettingsHandler)
            except:
                pass

        return oSettingsHandler

    def __updatePluginDB(self, data):
        file = open(self.pluginDBFile, 'w')
        json.dump(data,file)
        file.close()

    def __getPluginDB(self):
        if not os.path.exists(self.pluginDBFile):
            return dict()
        file = open(self.pluginDBFile, 'r')
        try:
            data = json.load(file)
        except ValueError:
            logger.error("pluginDB seems corrupt, creating new one")
            data = dict()
        file.close()
        return data

    def __updateSettings(self, pluginData):
        '''
        data (dict): containing plugininformations
        '''
        xmlString = '<plugin_settings>%s</plugin_settings>'
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.settingsFile)
        #find Element for plugin Settings
        pluginElem = False
        for elem in tree.findall('category'):
            if elem.attrib['label']=='30022':
                pluginElem = elem
                break
        if not pluginElem:
            logger.info('could not update settings, pluginElement not found')
            return False
        pluginElements = pluginElem.findall('setting')
        for elem in pluginElements:
            pluginElem.remove(elem)
        # add plugins to settings
        for pluginID in sorted(pluginData):
            plugin = pluginData[pluginID]
            subEl = ET.SubElement(pluginElem,'setting', {'type': 'lsep', 'label':plugin['name']})
            subEl.tail = '\n\t'
            attrib = {'default': 'false', 'type': 'bool'}
            attrib['id'] = 'plugin_%s' % pluginID
            attrib['label'] = plugin['name']
            subEl = ET.SubElement(pluginElem, 'setting', attrib)
            subEl.tail = '\n\t'
            if 'settings' in plugin:
                customSettings = []
                try:
                    customSettings = ET.XML(xmlString % plugin['settings']).findall('setting')
                except:
                    logger.info('Parsing of custom settings for % failed.' % plugin['name'])
                for setting in customSettings:
                    setting.tail = '\n\t'
                    pluginElem.append(setting)
        pluginElements = pluginElem.findall('setting')[-1].tail = '\n'
        try:
            ET.dump(pluginElem)
        except:
            logger.info('Settings update failed')
            return
        tree.write(self.settingsFile)

    def __getFileNamesFromFolder(self, sFolder):
        aNameList = []
        items = os.listdir(sFolder)
        for sItemName in items:
            if sItemName.endswith('.py'):
                sItemName = os.path.basename(sItemName[:-3])
                aNameList.append(sItemName)
        return aNameList

    def __getPluginData(self, fileName):
        pluginData = {}
        try:
            plugin = __import__(fileName, globals(), locals())
            pluginData['name'] = plugin.SITE_NAME
        except Exception, e:
            logger.error("Can't import plugin: %s :%s" % (fileName, e))
            return False
        try:
            pluginData['icon'] = plugin.SITE_ICON
        except:
            pass
        try:
            pluginData['settings'] = plugin.SITE_SETTINGS
        except:
            pass
        try:
            pluginData['version'] = plugin.SITE_VERSION
        except:
            pass
        return pluginData

    def checkForSiteUpdates(self):
        # ToDo: Add settings for UpdateCheck (Enabled/Disabled, Trusted Hosts,Download beta versions,...)
        if not cConfig().getSetting('auto_update'):
            return

        beta = cConfig().getSetting('auto_update_beta')

        addon_version = LooseVersion(common.addon.getAddonInfo('version'))

        trustedHosters = ["https://raw.githubusercontent.com/seberoth/plugin.video.xstream/site_updater/test_dir/master.json"]
        oRequest = cRequestHandler(trustedHosters[0], False)
        html = oRequest.request()
        json_data = json.loads(html)

        plugins = self.getAvailablePlugins()
        for plugin in plugins:
            if 'version' in plugin:
                if plugin['id'] in json_data['plugins']:
                    sitedata = json_data['plugins'][plugin['id']]
                    cur_version = LooseVersion(plugin['version'])
                    rel_version = LooseVersion(sitedata['release']['version'])

                    if beta:
                        beta_version = LooseVersion(sitedata['beta']['version'])
                        min_addon_version = LooseVersion(sitedata['beta']['need_main_version'])
                        if beta_version > cur_version and beta_version > rel_version and min_addon_version <= addon_version:
                            self.__downloadUpdate(plugin['id'], sitedata['beta']['url'])
                            logger.info("BetaUpdateDone")

                    min_addon_version = LooseVersion(sitedata['release']['need_main_version'])
                    if rel_version > cur_version and min_addon_version >= addon_version:
                        self.__downloadUpdate(plugin['id'], sitedata['release']['url'])

    def __downloadUpdate(self, id, url):
        oRequest = cRequestHandler(url, False)
        html = oRequest.request()

        try:
            path = os.path.join(self.defaultFolder, id + ".py")
            f = open(path, "w")
            f.write(html)
            f.close()
        except:
            pass
