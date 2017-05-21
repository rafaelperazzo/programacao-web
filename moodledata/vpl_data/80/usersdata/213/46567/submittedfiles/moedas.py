# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('Informe o valor a: '))
b=int(input('Informe o valor b: '))
c=int(input('Informe o valor c: '))

if (c%a)==0:
    print(c//a)
    print('0')
elif (c%a)!=0:
    print(c//a)
    if (c%b)==0:
        print(c//b)
    else:
        print('N')
        
'''
for i in range (0,c+1,1):
    if (c%a)==0:
        print(c//a)
    elif (c%b)==0:
        print(c//b)
    else:
'''