import dateutil.parser
import requests

source = 'sampledata.csv'
table = []

try:
    open(source)
except:
    print('This file cannot be opened')
else:
    with open(source) as f:
        source = csv.reader(f)
        for row in source:
            out = [dateutil.parser.parse(row[0]),row[1],row[2]]
            print(out)
            table.append(out)
