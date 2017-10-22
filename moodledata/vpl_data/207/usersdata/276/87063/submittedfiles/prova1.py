# -*- coding: utf-8 -*-
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

a = int (input('Digite a: '))
b = int (input('Digite b: '))
c = int (input('Digite c: '))
d = int (input('Digite d: '))
e = int (input('Digite e: '))

if (a>b) and (a>c) and (a>d) and (a>e) and (b>c) and (b>d) and (b>e) and (c>d) and (c>e) and (d>e):
    print ('C')
elif (e>a) and (e>b) and (e>c) and (e>d) and (d>a) and (d>b) and (d>c) and (c>a) and (c>b) and (b>a):
    print ('D')
else:
    print ('N')

