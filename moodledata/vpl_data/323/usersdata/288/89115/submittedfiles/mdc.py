# -*- coding: utf-8 -*-
import math
x=int(input('Digite um numero x: '))
y=int(input('Digite um numero y: '))
resto=(x%y)
while (x%y)!=0:
    x=y
    y=resto
    resto=x%y
    if resto==1:
        print (x%y)
    else:
        print (x//y)