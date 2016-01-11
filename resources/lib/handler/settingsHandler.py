from resources.lib import logger
from xml.etree import ElementTree
from xml.dom import minidom

class cSettingsHandler():
    def __init__(self):
        self.__data = dict()
        self.__data['childs'] = []
        pass

    def addSeperator(self, parent, visible = '', enable = '', subsetting = False):
        child = {'type': 'sep'}
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addLabelSeperator(self, parent, label, visible = '', enable = '', subsetting = False):
        child = {'type': 'lsep', 'label': label}
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addText(self, parent, id, label, option='', default = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'text', 'label': label}
        if option:
            child['option'] = option
        if default:
            child['default'] = default
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addIPAddress(self, parent, id, label, default = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'ipaddress', 'id': id, 'label': label}
        if default:
            child['default'] = default
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addNumber(self, parent, id, label, default = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'number', 'id': id, 'label': label}
        if default:
            child['default'] = default
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addSlider(self, parent, id, label, range, option, default = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'slider', 'id': id, 'label': label, 'range': range, 'option': option}
        if default:
            child['default'] = default
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addDate(self, parent, id, label, default = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'date', 'id': id, 'label': label}
        if default:
            child['default'] = default
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addTime(self, parent, id, label, default = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'time', 'id': id, 'label': label}
        if default:
            child['default'] = default
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addBool(self, parent, id, label, default = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'bool', 'id': id, 'label': label}
        if default:
            child['default'] = default
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addSelect(self, parent, id, label, values, visible = '', enable = '', subsetting = False):
        # ToDo: values or lvalues
        child = {'type': 'select', 'id': id, 'label': label, 'values': values}
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addAddon(self, parent, id, label, addontype, multiselect = None, visible = '', enable = '', subsetting = False):
        child = {'type': 'addon', 'id': id, 'label': label, 'addontype': addontype}
        if multiselect is not None:
            if multiselect:
                child['multiselect'] = 'true'
            else:
                child['multiselect'] = 'false'
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addEnum(self, parent, id, label, values, visible = '', enable = '', subsetting = False):
        # ToDo: values or lvalues
        # Make values to list?
        child = {'type': 'enum', 'id': id, 'label': label, 'values': values}
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addLabelEnum(self, parent, id, label, values, sort=False, visible = '', enable = '', subsetting = False):
        # Make values to list?
        child = {"type": 'labelenum', 'id': id, 'label': label, 'values': values}
        if sort:
            child['sort'] = 'yes'
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addFile(self, parent, id, label, value = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'file', 'id': id, 'label': label}
        if value:
            child['value'] = value
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addAudio(self, parent, id, label, value = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'audio', 'id': id, 'label': label}
        if value:
            child['value'] = value
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addVideo(self, parent, id, label, value = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'video', 'id': id, 'label': label}
        if value:
            child['value'] = value
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addImage(self, parent, id, label, value = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'image', 'id': id, 'label': label}
        if value:
            child['value'] = value
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addExecutable(self, parent, id, label, value = '', visible = '', enable = '', subsetting = False):
        child = {'type': 'executable', 'id': id, 'label': label}
        if value:
            child['value'] = value
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addFolder(self, parent, id, label, source='auto', value='', option='', visible = '', enable = '', subsetting = False):
        child = {'type': 'folder', 'id': id, 'label': label}
        if source != 'auto':
            child['source'] = source
        if value:
            child['value'] = value
        if option:
            child['option'] = option
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addFileEnum(self, parent, id, label, values, mask='', option='', visible = '', enable = '', subsetting = False):
        # Make values to list?
        child = {"type": 'labelenum', 'id': id, 'label': label, 'values': values}
        if mask:
            child['mask'] = 'mask'
        if option:
            child['option'] = 'option'
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addAction(self, parent, id, label, action, close = False, visible = '', enable = '', subsetting = False):
        child = {"type": 'labelenum', 'id': id, 'label': label, 'action': action}
        if close:
            child['option'] = 'close'
        child = self.__parseOptionalAttributes(child, visible, enable, subsetting)
        self.addRaw(parent, child)

    def addCategory(self, label, id=None):
        if id is None:
            id = label
        child = {'attr': {'label': label}, 'type': 'category', 'id': id}
        self.__data['childs'].append(child)

    def addRaw(self, parent, data):
        child = {'attr': data}
        self.__addToParent(self.__data, parent, child)

    def parseSiteSettings(self, pluginID, settings):
        for entry in settings:
            entry['id'] = '%s-%s' % (pluginID, entry['id'])
            self.addRaw('site_settings', entry)

    def compile(self):
        try:
            xmlDoc = ElementTree.TreeBuilder()
            xmlDoc.start('settings', {})
            self.__generateFile(self.__data, xmlDoc)
            xmlDoc.end('settings')
            return self.__prettify(xmlDoc.close())
        except:
            return None

    def __parseOptionalAttributes(self, child, visible = '', enable = '', subsetting = False):
        if visible:
            child['visible'] = visible
        if enable:
            child['enable'] = enable
        if subsetting:
            child['subsetting'] = 'true'
        return child


    def __prettify(self, elem):
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def __addToParent(self, data, parent, child):
        for entry in data['childs']:
            id = None

            logger.info('SetDebug: %s' % entry)

            if 'id' in entry:
                id = entry['id']
            elif 'id' in entry['attr']:
                id = entry['attr']['id']

            if id and id == parent:
                if 'childs' not in entry:
                    entry['childs'] = []
                entry['childs'].append(child)
            elif 'childs' in entry:
                self.__addToParent(entry, parent, child)

    def __generateFile(self, data, xmlDoc):
        if 'childs' not in data: return
        for entry in data['childs']:
            # ToDo: Handle special cases
            if 'type' in entry:
                type = entry['type']
            elif 'type' in entry['attr']:
                type = entry['attr']['type']

            if type == 'category':
                xmlDoc.start('category', entry['attr'])
                self.__generateFile(entry, xmlDoc)
                xmlDoc.end('category')
            else:
                xmlDoc.start('setting', entry['attr'])
                xmlDoc.end('setting')
