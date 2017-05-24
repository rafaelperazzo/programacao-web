# -*- coding: utf-8 -*-
import math
a=int(input('Digite um número: '))
b=int(input('Digite um número: '))
ndedivisoes=0
if b>a:
    mdc=a
elif a>b:
    mdc=b
while a%mdc!=0 or b%mdc!=0:
    mdc=mdc-1
    ndedivisoes=ndedivisoes+1
print(mdc)    
print(ndedivisoes)
