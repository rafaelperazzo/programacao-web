# -*- coding: utf-8 -*-
from __future__ import division
c=int(input('digite o valor da cédula:'))
a=int(input('digite o valor da moeda a:'))
b=int(input('digite o valor da moeda b:'))

cont=0
i=1

while c>0:
    if c%4=0 or c%2=0:
        cont=cont+i
        i=i+1
print(cont)        