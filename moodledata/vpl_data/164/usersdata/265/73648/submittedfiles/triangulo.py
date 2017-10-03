# -*- coding: utf-8 -*-
import math
a=int(input('digite a: '))
b=int(input('digite b: '))
c=int(input('digite c: '))
if ((a**2)==((b**2)+(c**2))):
    print('S')
    print('Re')
elif ((a**2)>((b**2)+(c**2))):
    print('S')
    print('Ob')
elif ((a**2)==((b**2)+(c**2))):
    print('S')
    print('Ac')
elif (a==b==c):
    print('S')
    print('Eq')
elif (b==c!=a):
    print('S')
    print('Is')
elif (a!=b!=c):
    print('S')
    print(Es')
else :
    print('N')