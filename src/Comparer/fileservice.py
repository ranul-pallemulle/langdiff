import json

class FileReader:
    def __init__(self, argv):
        self.filenames = argv[1:]

    def readJson(self):
        content = []
        for name in self.filenames:
            with open(name, 'r') as file:
                content.append(json.load(file))
        return content
