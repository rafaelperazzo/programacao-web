# -*- coding: utf-8 -*-
from __future__ import division

a=int(input('Digite o valor da moeda:'))
b=int(input('Digite o valor da moeda:'))
c=int(input('Digite o valor da cédula:'))
na=0
nb=0
cont=0

while na<=c//a:
    nb=(c-na*a)//b
    if na*a +nb*b==c:
        cont+=1
        break
    else:
        na+=1
if cont>0:
    print na
    print nb
else:
    print('N')