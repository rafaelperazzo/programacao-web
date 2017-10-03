# -*- coding: utf-8 -*-
import math
a=int(input('A:'))
b=int(input('A:'))
c=int(input('A:'))
d=int(input('A:'))

cont = 0

if a>d and a>b:
    cont =cont + 1
if b>a and b>c:
    cont =cont + 1
if c>d and c>b:
    cont =cont + 1
if d>a and d>c:
    cont =cont + 1

if cont == 1:
    print ('S')
else: 
    print ('N')