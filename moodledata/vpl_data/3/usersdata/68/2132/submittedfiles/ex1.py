from __future__ import division

#ENTRADA:
a = ('Digite a:')
b = ('Digite b:')
c = ('Digite c:')
Delta = b**2 - 4*a*c
x1 = (-b + (Delta)**0.5)/ (2*a)
x2 = (-b - (Delta)**0.5)/ (2*a)

if Delta>=0:
   print x1 and x2
else :
    print ('SRR')
    
