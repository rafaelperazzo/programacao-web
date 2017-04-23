# -*- coding: utf-8 -*-
a=float(input('Digite um número:'))
b=float(input('Digite um número:'))
c=float(input('Digite um número:'))
d=float(input('Digite um número:'))

#Maior

if a>b and a>c and a>d:
    print(a)
elif b>a and b>c and b>d:
    print (b)
elif c>a and c>b and c>d:
    print (c)
else:
    print (d)
    
#Menor

if a<b and a<c and a<d:
    print (a)
elif b<a and b<c and b<d:
    print (b)
elif c<a and c<b and c<d:
    print (c)
else:
    print (d)
