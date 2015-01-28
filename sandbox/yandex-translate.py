from pprint import pprint
from urllib.parse import unquote, quote
import json
from urllib.parse import urlencode
from urllib.request import urlopen
import itertools


def translate(text):
    api_link = "https://translate.yandex.net/api/v1.5/tr.json/translate?" \
           "key=trnsl.1.1.20150127T182316Z.dbc14b07439f9b54.ea85695d637fb907bedfbbc24119e75d52a08e0c" \
           "&text={}" \
           "&lang=en-ru" \
           "&[format=plain" \
           # "&[options=<опции перевода>]" \
           # "&[callback=<имя callback-функции>]"
    quoted_query = quote(text)
    active_url = api_link.format(quoted_query)
    response = urlopen(active_url).read().decode('utf-8')
    translated = json.loads(response)
    grabbed = translated['text'][0]
    split_grabbed = grabbed.split()
    # print(grabbed)
    # print(split_grabbed)
    # print(min(split_grabbed, key=len))
    return split_grabbed[0], split_grabbed[1]


# def main():
en_collig = [['depend', 'on'], ['rely', 'on']]
# query = "depend on"
enru = []
mixed = []
ruverbs = []
rupreps = []

for english in en_collig:
    query = english[0] + ' ' + english[1]
    # print(item)
    # print(translate(query))
    ruverb, ruprep = translate(query)
    russian = [ruverb, ruprep]
    enru.append([english, russian])
    ruverbs.append(ruverb)
    rupreps.append(ruprep)
for p in rupreps:
    mixed.append([[v, p] for v in ruverbs if (v, p) not in list(zip(ruverbs, rupreps))])

print('MIXED', list(itertools.chain(*mixed)))
