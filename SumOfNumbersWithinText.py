
###11.1 calculate the sum of the numbers within a text
import re
hand = open ('regex_sum_236287.txt')
stufflist=list()
numlist=list()
for line in hand:
    line = line.rstrip()
    stuff=re.findall('[0-9]+', line)
    if len(stuff)>=1:
        for number in stuff:
            num=float(number)
            numlist.append(num)
print sum(numlist)
