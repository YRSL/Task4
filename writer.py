from abc import ABC, abstractmethod
from xml.dom.minidom import parseString
import json
import dicttoxml


class Writer(ABC):

    @abstractmethod
    def write(self, *args):
        pass


class JsonWriter(Writer):

    def write(self, filename, data):
        with open(filename + ".json", 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, default=str)


class XmlWriter(Writer):

    def write(self, filename, data):
        result = parseString(dicttoxml.dicttoxml(data)).toprettyxml()
        with open(filename + ".xml", 'w') as file:
            file.write(str(result))
