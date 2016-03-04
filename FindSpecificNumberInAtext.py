####Assigment 7.2
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count=0
word=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    startpos=line.find(':')  
    endpos=line.find('\n')
    word=word+float(line[startpos+1:endpos])
    count=count+1
    average=word/count
    
print "Average spam confidence:", average
