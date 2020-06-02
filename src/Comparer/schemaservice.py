import json
class SchemaComparer:
    def __init__(self, argv):
        self.json = argv

    def getSchema(self, i):
        return self.flatten(self.json[i]).keys()

    def hasSameSchema(self, i, j):
        return sorted(self.getSchema(i)) == sorted(self.getSchema(j))

    def diff(self, i, j):
        resultset = dict()
        first = self.flatten(self.json[i])
        second = self.flatten(self.json[j])
        for key in first:
            if first[key] != second[key]:
                resultset[key] = [first[key], second[key]]
        return resultset

    def flatten(self, json, jpath='$'):
        jpathvaluepairs = dict()
        if isinstance(json, list):
            for i, value in enumerate(json, start=0):
                newpath = jpath + '[{}]'.format(i)
                jpathvaluepairs = dict(jpathvaluepairs, **self.flatten(value, newpath))
        elif isinstance(json, dict):
            for key in json:
                newpath = jpath + '.' + "['{}']".format(key) if '.' in key else jpath + '.' + key
                jpathvaluepairs = dict(jpathvaluepairs, **self.flatten(json[key], newpath))
        else:
            new = {jpath: json}
            jpathvaluepairs = dict(jpathvaluepairs, **new)
        return jpathvaluepairs