# -*- coding: utf-8 -*-
import math
x=int(input('digite um numero qualquer:'))
y=int(input('digite um numero menor que o digitado anteriormente:'))
contador=0
while x%y!=0:
    resto=x%y
    x=y
    y=resto
    contador=contador+1
    mdc=resto
print(mdc)
print(resto)