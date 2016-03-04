fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
lst2 = list()
lstsecond=list()

for line in fh:
    line.rstrip()
    words=line.split()
    lst.extend(words)
   
for words in lst:
    if words not in lst2:
        lst2.append(words)

print sorted(lst2)
