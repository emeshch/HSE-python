from urllib.request import urlopen
import re
# from pprint import pprint
from lxml.html import fromstring, tostring

# page = urlopen("http://www.hse.ru/org/persons/?search_person=%D0%B0%D0%B1%D0%B0%D0%BD%D0%BA%D0%B8%D0%BD%D0%B0").read().decode('utf-8')
page = open("hse.html").read()
doc = fromstring(page)
people = doc.find_class("post person")

for man in people:
    info = tostring(man)
    ans = str(info)
    # print('to string', type(ans))
    tels = re.findall(r'((\+7 \(\d{3}\) )?\d{3}(-\d{2}){2})', ans)
    tel_numbers = [tel[0] for tel in tels]
    print('num', tel_numbers)
    # print(info)
    print('--------')
# class Person(object):
#     def __init__(self, name):
#         self.name = name




print("=====================================")


