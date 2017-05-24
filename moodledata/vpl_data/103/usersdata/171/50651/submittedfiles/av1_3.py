# -*- coding: utf-8 -*-
import math
x=int(input('digite um numero qualquer:'))
y=int(input('digite um numero menor que o digitado anteriormente:'))
contador=1
mdc=y
resto=x%y
while x%y>0:
    resto da divisao =x%y
    x=y
    y=resto da divisao 
    mdc=resto da divisao
    contador=contador+1
print( mdc )
print(contador)