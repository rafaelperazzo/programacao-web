# -*- coding: utf-8 -*-
import math
z=int(input('digite um numero qualquer:'))
y=int(input('digite um numero menor que o digitado anteriormente:'))
contador=1
mdc=y
resto=z%y
while z%y>0:
    resto=z%y
    z=y
    y=resto
    mdc=resto
    contador=contador+1
print( mdc )
print(contador)