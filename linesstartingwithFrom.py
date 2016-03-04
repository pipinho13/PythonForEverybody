####8.2

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
count = 0
fh = open(fname)
for line in fh:
    line=line.rstrip()
    if line=='': continue
    words=line.split()
    if words[0]!='From': continue
    count=count+1    
    print words[1]
    


print "There were", count, "lines in the file with From as the first word"
