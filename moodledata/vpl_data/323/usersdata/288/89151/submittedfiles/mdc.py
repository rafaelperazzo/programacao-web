# -*- coding: utf-8 -*-
import math
x=int(input('Digite um numero x: '))
y=int(input('Digite um numero y: '))
a=x
b=y
resto = a%b
while (x%y)!=0:
    a=b
    b=resto
    resto=(a%b)
    print ('%d' %b)