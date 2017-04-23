# -*- coding: utf-8 -*-
a=float(input('Digite N1:'))
b=float(input('Digite N2:'))
c=float(input('Digite N3:'))

if a<b and b<c:
     print(a)
     print(b)
     print(c)
     
elif a<c and c<b:
    print(a)
    print(c)
    print(b)
    
elif b<c and c<a:
    print(b)
    print(c)
    print(a)
    
elif b<a and a<c:
    print(b)
    print(a)
    print(c)
    
elif c<b and b<a:
    print(c)
    print(a)
    print(b)
    
else:
    print(c)
    print(a)
    print(b)
    