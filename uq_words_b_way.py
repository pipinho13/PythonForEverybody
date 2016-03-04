###Assigment 8.1
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    words=line.split()
    lst.extend(words)
    
output=list(set(lst))
output.sort()
print output
