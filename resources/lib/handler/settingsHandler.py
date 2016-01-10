from resources.lib import logger
from xml.etree import ElementTree
from xml.dom import minidom

class cSettingsHandler():
    def __init__(self):
        self.__data = dict()
        self.__data['childs'] = []
        pass

    def addSeperator(self, parent, label = ''):
        child = {'attr': {"type": "sep", "label": label}}
        self.__addToParent(self.__data, parent, child)

    def addText(self, parent, id, label, default, enable='', option=''):
        child = {'attr': {"type": "text", "id": id, "label": label, "default": default}}
        if enable:
            child['attr']['enable'] = enable
        if option:
            child['attr']['option'] = option
        self.__addToParent(self.__data, parent, child)

    def addCategory(self, label, id=None):
        if id is None:
            id = label
        child = {'attr': {"label": label}, "type": "category", "id": id}
        self.__data['childs'].append(child)

    def addBool(self, parent, id, label, default, enable=''):
        self.__addSetting("bool", parent, id, label, default, enable)

    def addNumber(self, parent, id, label, default, enable=''):
        self.__addSetting("number", parent, id, label, default, enable)

    def addEnum(self, parent, id, label, default, values, enable=''):
        # Make values to list?
        child = {'attr': {"type": 'enum', "id": id, "label": label, "default": default, "values": values}}
        if enable:
            child['attr']['enable'] = enable
        self.__addToParent(self.__data, parent, child)

    def addFolder(self, parent, id, label, default, enable=''):
        self.__addSetting("folder", parent, id, label, default, enable)

    def compile(self):
        logger.info("SettingsDebug: %s" % self.__data)
        xmlDoc = ElementTree.TreeBuilder()
        xmlDoc.start('settings', {})
        self.__generateFile(self.__data, xmlDoc)
        xmlDoc.end('settings')
        return self.__prettify(xmlDoc.close())

    def __prettify(self, elem):
        """Return a pretty-printed XML string for the Element.
        """
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def __addSetting(self, type, parent, id, label, default, enable):
        child = {'attr': {"type": type, "id": id, "label": label, "default": default}}
        if enable:
            child['attr']['enable'] = enable
        self.__addToParent(self.__data, parent, child)

    def __addToParent(self, data, parent, child):
        for entry in data['childs']:
            if 'id' in entry:
                id = entry['id']
            elif 'id' in entry['attr']:
                id = entry['attr']['id']

            if id == parent:
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
