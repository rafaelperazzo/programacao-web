# -*- coding: utf-8 -*-
import math
f=int(input('digite o valor de f:'))
g=int(input('digite o valor de g:'))
h=int(input('digite o valor de h:'))
if f<g+h:
    print('S')
    if (f**2)==(g**2)+(h**2):
        print('RE')
    if (f**2)>(g**2)+(h**2):
        print('OB')
    if (f**2)<(g**2)+(h**2):
        print('AC')
    if f==g==h:
        print('EQ')
    if g==h!=f:
        print('IS')
    if f!=g!=h:
        print('ES')
else:
    print('N')
