def computepay(h,r):
   if h<=40:
       result=h*r
   elif h>40:
       result=40*r+(h-40)*r*1.5
   return result

hrs = raw_input("Enter Hours:")
rate = raw_input("Rate:")
h=float(hrs)
r=float(rate)
p = computepay(h,r)
print p
