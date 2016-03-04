	
####10.2 Write a program to read through the mbox-short.txt and figure out the distribution
#### by hour of the day for each of the messages. You can pull the hour out from the 'From ' 
#### line by finding the time and then splitting the string a second time using a colon.	

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
for line in handle:
    line=line.rstrip()
    if line=='': continue
    words=line.split()
    if words[0]!='From': continue
    lst.append(words[5])
lst2=list()
for time in lst:
    hours=time.split(":")
    lst2.append(hours[0])
counts=dict()
for hours in lst2:
    counts[hours]=counts.get(hours,0)+1
lst3=list()
for key, val in counts.items():
    lst3.append((key, val))

lst3.sort()
for key, val in lst3:
    print key, val
