# -*- coding: utf-8 -*-
import math
x=int(input('Digite um numero x: '))
y=int(input('Digite um numero y: '))
resto=(x%y)
while (resto)!=0:
    a=(resto/y)
    if resto<y:
        break
print (a)
