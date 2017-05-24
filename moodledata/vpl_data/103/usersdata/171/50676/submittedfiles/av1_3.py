# -*- coding: utf-8 -*-
import math
z=int(input('digite um numero qualquer:'))
w=int(input('digite um numero menor que o digitado anteriormente:'))
contador=1
mdc=w
resto=z%w
while z%w>0:
    resto=z%w
    z=w
    z=resto
    mdc=resto
    contador=contador+1
print( mdc )
print(contador)