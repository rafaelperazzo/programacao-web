# -*- coding: utf-8 -*-
a=float(input('Digite um numero:'))
b=float(input('Digite um numero:'))
c=float(input('Digite um numero:'))
d=float(input('Digite um numero:'))

if a>b and a>c:
    print (a)
    
elif b>a and b>c: 
    print(b)
    
elif c>a and c>b and c>d:
    print(c)

else:
    print (d)
    
if a<b and a<c and a<d:
    print(b)
    
elif c<a and c<b and c<d:
    print(a)
    
elif b<a and b<c and b<d:
    print (b)

elif c<a and c<b and c<d:
    print (c)
    
else:
    print(d)
    
    
    
    



