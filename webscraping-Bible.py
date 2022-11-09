import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

'''
#https://ebible.org/asv/JHN01.htm

webpage = 'https://ebible.org/asv/JHN'


chapter = random.randint(1,21)
num = str(chapter)

if chapter < 10:
    num = '0' + str(chapter) 

webpage = webpage + num + '.htm'
print(webpage)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)


webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll('div', class_ = 'main')

verse_list = {}

for verse in page_verses:
    verse_list = verse.text.split('.')

myverse = 'Chapter: ' + num + ' Verse:' + random.choice(verse_list[:len(verse_list)-2])
print(myverse)
'''



#new website

#https://biblehub.com/asv/john/10.htm

webpage = 'https://biblehub.com/asv/john/'


chapter = random.randint(1,21)
webpage = webpage + str(chapter) + '.htm'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)


webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll('div', class_ = 'chap')

verse_list = {}

for verse in page_verses:
    verse_list = verse.text.split('.')

myverse = 'Chapter: ' + str(chapter) + ' Verse: ' + random.choice(verse_list[:len(verse_list)-2])
print(myverse)