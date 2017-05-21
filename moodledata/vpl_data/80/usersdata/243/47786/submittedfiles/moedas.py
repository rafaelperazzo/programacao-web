# -*- coding: utf-8 -*-
from __future__ import division
c=int(input('digite o valor da cédula:'))
a=int(input('digite o valor da moeda a:'))
b=int(input('digite o valor da moeda b:'))

cont=0


while ((c//a) or (c//b))>0:
    if c%a==0 or c%b==0:
    cont=cont+1
    c=c//a
    c=c//b
print(cont)        

    
        