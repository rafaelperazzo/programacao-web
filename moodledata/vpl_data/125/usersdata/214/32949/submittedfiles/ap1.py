# -*- coding: utf-8 -*-
a= float(input('Digite valor de a:'))
b= float(input('Digite valor de b:'))
c= float(input('Digite valor de c:'))

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

elif c<a and a<b:
    print(a)
    print(c)
    print(b)
    
elif c<b and b<a:
    print(a)
    print(c)
    print(b)
    
else:
   print(c)
   print(a)
   print(b)