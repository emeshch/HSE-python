from urllib.request import urlopen
from urllib.robotparser import RobotFileParser
import re
import shutil
import os
from bs4 import BeautifulSoup

homedir = '/home/name/Desktop/mesh'
def clear_dir(dir2clear=homedir):
    os.chdir(dir2clear)
    dirs = [i for i in os.listdir('.') if os.path.isdir(i) and i.startswith('_')]
    #print(dirs)
    for i in dirs:
        shutil.rmtree(i)
clear_dir()
exit()

# home = os.getcwd()
domain = 'http://newsru.com'

robots = RobotFileParser()
robots.set_url('http://newsru.com/robots.txt')
robots.read()
outer_urls = []

def grab_from(url):
    links_to = []
    page = urlopen(url).read().decode('windows-1251')
    all_links = re.findall('href=["\']([^"\']*)["\']', page)
    # print('on the page: ', url, 'found: ', all_links)
    for link in all_links:
        if link.startswith('//') or link.startswith('/promo') or link.startswith('/info') or link.startswith('#'):
            continue
        if link.startswith("http://") or link.startswith("https://"):
            outer_urls.append(link)
            continue
        if not robots.can_fetch('*', link):
            print('robots can not fetch' + link)
            continue
        if link.startswith("/") and link != '/':
            links_to.append(link)
    # print(links_to)
    return list(set(links_to))

def grab_news(news_page):
    soup = BeautifulSoup(news_page)
    return soup.title.string

on_main = grab_from('http://newsru.com')
home = '/home/name/Desktop/mesh'
for link in on_main:
    # link = domain + link
    name = re.sub('/', '_', link)
    # print(name)
    if re.match(r'[\w^_]+_\w+', name) and not os.path.exists(home + '/' + name):
        os.mkdir(home + '/' + name)
        os.chdir(home + '/' + name)
        news_page = urlopen(domain + link).read().decode('windows-1251')
        title = grab_news(news_page)
        file = open(home + '/' + name + "/news.txt", "w")
        file.write(title)
        file.close()
        os.chdir(home)

# if url in match:
#     continue
# match.append(url)



