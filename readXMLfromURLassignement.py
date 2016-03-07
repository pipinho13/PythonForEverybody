
###assignement 1 week5
import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
uh = urllib.urlopen(url)
count=0
countlist=list()
data = uh.read()
## print data
tree = ET.fromstring(data)
results = tree.findall('comments/comment')



for item in results:
    counts=item.find('count').text
    num=float(counts)
    countlist.append(num)
    count=count+1
    print counts
print count
print sum(countlist)


