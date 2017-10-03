# -*- coding: utf-8 -*-
import math
a = float(input('Forneça o maior valor, se existir: '))
b = float(input('Forneça o segundo maior valor, se existir: '))
c = float(input('Forneça o menor valor: '))
print()
if (b+c)<=a:
    print('N')
else:
    print('S')
    if a*a==b*b+c*c:
        print('Re')
    if a*a>b*b+c*c:
        print('Ob')
    if a*a<b*b+c*c:
        print('Ac')
    if a==b and a==c:
        print('Eq')
    if b==c and b!=c:
        print('Is')
    if a!=b and a!=c and b!=c:
        print('Es')
