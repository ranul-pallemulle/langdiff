import sys
from fileservice import FileReader
from schemaservice import SchemaComparer
def main(argv):
    reader = FileReader(argv)
    comparer = SchemaComparer(reader.readJson())
    eqSchema = comparer.hasSameSchema(0, 1)
    print('Equivalent schema: {}'.format(eqSchema))
    if eqSchema:
        print(comparer.diff(0, 1))
    

if __name__ == '__main__':
    main(sys.argv)