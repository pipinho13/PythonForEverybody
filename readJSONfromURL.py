

###assignement 1 week6
###http://python-data.dr-chuck.net/comments_42.json
import urllib
import json

url = raw_input('Enter location: ')
uh = urllib.urlopen(url)


countlist=list()
data = uh.read()
## print data
info=json.loads(str(data))
length=len(info['comments'])


for i in range(0, length):
    num=info['comments'][i]['count']
    num=float(num)
    countlist.append(num)
print length
print sum(countlist)
