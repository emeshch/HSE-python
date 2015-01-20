from xml.etree import ElementTree
from urllib.request import urlopen

# url = 'http://search.ruscorpora.ru/search.xml?env=alpha&mycorp=&mysent=&mysize=&mysentsize=&mydocsize=&spd=&' \
#       'text=lexgramm&mode=main&sort=gr_tagging&lang=ru&nodia=1&parent1=0&' \
#       'level1=0&lex1=&gramm1=ADV&sem1=&sem-mod1=sem&sem-mod1=sem2&flags1=&m1=&parent2=0&' \
#       'level2=0&min2=1&max2=1&lex2=&gramm2=A&sem2=&sem-mod2=sem&sem-mod2=sem2&flags2=&m2='
url = input('url = ')
fixed_url = url.replace('search.xml', 'dump.xml')
tree = ElementTree.parse(urlopen(fixed_url))
answer = []
index = 0
for word in tree.findall('.//word[@queryPosition]'):
    answer.append(word.get('text'))
for index in range(0, len(answer)-1, 2):
    print(answer[index], ' ', answer[index+1])



