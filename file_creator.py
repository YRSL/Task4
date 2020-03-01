from writer import JsonWriter, XmlWriter


class FileCreator:

    def __init__(self, file_format):
        if file_format == "json":
            self.writer = JsonWriter()
        elif file_format == "xml":
            self.writer = XmlWriter()

    def create_file(self, name, data):
        self.writer.write(name, data)
