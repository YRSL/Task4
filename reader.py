from abc import ABC, abstractmethod
import json


class Reader(ABC):

    @abstractmethod
    def read(self, *args):
        pass


class JsonReader(Reader):

    @staticmethod
    def read(json_file):
            with open(json_file, encoding='UTF-8') as file:
                data = json.load(file)
            return data
