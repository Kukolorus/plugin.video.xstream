class cSettingsHandler():
    def __init__(self):
        self.__data = dict()
        self.__data['childs'] = []
        pass

    def addSeperator(self, parent):
        child = {"type": "sep"}
        self.__addToParent(self.__data, parent, child)

    def addCategory(self, label, id=None):
        if id is None:
            id = label
        child = {"type": "category", "id": id, "label": label}
        self.__data['childs'].append(child)

    def addBool(self, parent, id, label, default, enable=''):
        self.__addSetting("bool", parent, id, label, default, enable)

    def addNumber(self, parent, id, label, default, enable=''):
        self.__addSetting("number", parent, id, label, default, enable)

    def addEnum(self, parent, id, label, default, values, enable=''):
        # Make values to list?
        child = {"type": type, "id": id, "label": label, "default": default, "values": values}
        if enable != '':
            child['enable'] = 'enable="%s"' % enable
        else:
            child['enable'] = ''
        self.__addToParent(self.__data, parent, child)

    def compile(self):
        xml = '<settings>\n'
        xml += self.__generateFile(self.__data)
        xml += '</settings>'
        return xml

    def __addSetting(self, type, parent, id, label, default, enable):
        child = {"type": type, "id": id, "label": label, "default": default}
        if enable != '':
            child['enable'] = 'enable="%s"' % enable
        else:
            child['enable'] = ''
        self.__addToParent(self.__data, parent, child)

    def __addToParent(self, data, parent, child):
        for entry in data['childs']:
            if entry['id'] == parent:
                if 'childs' not in entry:
                    entry['childs'] = []
                entry['childs'].append(child)
            else:
                if 'childs' in entry:
                    self.__addToParent(entry, parent, child)

    def __generateFile(self, data, indent=1):
        xml = ''
        if 'childs' in data:
            for entry in data['childs']:
                # ToDo: Handle special cases
                if entry['type'] == 'category':
                    xml += ('\t' * indent) + '<category label="%s">\n' % entry['label']
                    xml += self.__generateFile(entry, indent + 1)
                    xml += ('\t' * indent) + '</category>\n'
                elif entry['type'] == 'enum':
                    xml += (
                           '\t' * indent) + '<setting default="%s" %s id="%s" label="%s" type="%s" values="%s" />\n' % (
                    entry['default'], entry['enable'], entry['id'], entry['label'], entry['type'], entry['values'])
                elif entry['type'] == 'sep':
                    xml += ('\t' * indent) + '<setting type="sep" />\n'
                else:
                    xml += ('\t' * indent) + '<setting default="%s" %s id="%s" label="%s" type="%s" />\n' % (
                    entry['default'], entry['enable'], entry['id'], entry['label'], entry['type'])
        return xml
