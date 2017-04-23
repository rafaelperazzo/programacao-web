# -*- coding: utf-8 -*-
a=float(input('Digite um peso:'))
b=float(input('Digite um peso:'))
c=float(input('Digite um peso:'))
d=float(input('Digite um peso:'))

if (a==b+c+d) and (b+c==d) and (b==c):
    print('S')
else:
    print('N')