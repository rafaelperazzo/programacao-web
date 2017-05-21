# -*- coding: utf-8 -*-
a=float(input('Digite o valor a: '))
b=float(input('Digite o valor b: '))  
c=float(input('Digite o valor c: '))  
d=float(input('Digite o valor d: '))  

if a==b+c+d and b+c==d and b==c:
    print('S')
else:
    print('N')
