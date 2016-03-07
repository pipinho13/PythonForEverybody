
###Assessment2 Week4  
import urllib
from BeautifulSoup import *
position=0
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
counter=6

tags = soup('a')
for tag in tags:
    position=position+1
    tag.get('href', None)
    if position==18: html2=tag.get('href', None)


for x in range(0,counter):
    html = urllib.urlopen(html2).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    position=0
    for tag in tags:
         position=position+1
         tag.get('href', None)
         if position==18: html2=tag.get('href', None)
    print html2
