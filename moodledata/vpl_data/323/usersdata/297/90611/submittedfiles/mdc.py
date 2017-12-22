# -*- coding: utf-8 -*-
import math
x=int(input('digite um numero inteiro positivo: ))
y=int(input('digite um numero inteiro positivo: ))
mdc=x
while x<1 :
    x=int(input('digite um numero inteiro positivo: ))
while y<1 :
    y=int(input('digite um numero inteiro positivo: ))
while mdc%x!=0 or mdc%y!=0 :
    mdc=mdc-1
print('%d'%mdc')