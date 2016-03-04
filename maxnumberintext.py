
text = "X-DSPAM-Confidence:    0.8475"
pos=text.find('0')
text[pos:]
largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        number=int(num)
	
        
    except:
        print "Invalid input"
    if largest is None or number>largest:
       largest=number
    if smallest is None or number<smallest:
       smallest=number

print "Maximum is", largest
print "Minimum is", smallest
