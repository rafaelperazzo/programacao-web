# -*- coding: utf-8 -*-
import math
a=float(input('Informe o lado a: '))
b=float(input('Informe o lado b: '))
c=float(input('Informe o lado c: '))

if a<(b+c):
    print('S')
    if (a**2)==((b**2)+(c**2)):
        print('Re')
    elif (a**2)>((b**2)+(c**2)):
        print('Ob')
    elif (a**2)<((b**2)+(c**2)):
        print('Ac')
    if a==b and b==c:
        print('Eq')
    elif b==c and c!=a:
        print('Is')
    elif a!=b and b!=c:
        print('Es')
else:
    print('N')