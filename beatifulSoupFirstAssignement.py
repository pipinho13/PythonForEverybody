###Assessment Week4  
import urllib
from BeautifulSoup import *
numlist=list()
count=0
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags=soup('span')
for tag in tags:
     stuff= tag.contents[0]
     num=float(stuff)
     numlist.append(num)
     count=count+1
print count
print sum(numlist)
