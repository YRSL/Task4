from abc import ABC, abstractmethod
import json


class Writer(ABC):

    @abstractmethod
    def write(self, *args):
        pass


class JsonWriter(Writer):

    @staticmethod
    def write(list_objects):
        data_result = [i.to_dict() for i in list_objects]
        with open("result.json", 'w', encoding='UTF-8') as file:
            json.dump(data_result, file, sort_keys=True, indent=3)


class XmlWriter(Writer):

    @staticmethod
    def write(root):

        with open("result.xml", 'wb') as file:
            file.write(root)
