# -*- coding: utf-8 -*-
from __future__ import division
c=int(input('digite o valor da cédula:'))
a=int(input('digite o valor da moeda a:'))
b=int(input('digite o valor da moeda b:'))

cont=0
quantidade_a=c//a
quantidade_b=0

while quantidade_a>=0:
    troco=c-quantidade_a*a
    if troco%b==0:
        quantidade_b=troco//b
        cont=cont+1
        break
    else:
        quantidade_a=quantidade_a-1
if cont>0:
    print (quantidade_a)
    print (quantidade_b)
else:
    print('N')

      

    
        