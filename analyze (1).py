import json
import csv
from pprint import pprint

with open('data.json') as fp:
    a = json.load(fp)


data = a['snapshot']
# pprint(data)

i = 0
# ['shortDescription']['values'][0]['value']

with open('items.csv','w', encoding="latin-1") as fil:
    for items in data:
        i+=1
        lines = items['shortDescription']['values'][0]['value']
        fil.write('"')
        fil.write(lines)
        fil.write('",')
        fil.write('"')
        fil.write(lines.partition(' ')[0])
        fil.write(lines.partition(' ')[-1])
        fil.write('"')
        fil.write('\n')

fil.close()
fp.close()
