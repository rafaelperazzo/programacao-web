# -*- coding: utf-8 -*-
from __future__ import division
c=int(input('digite o valor da cédula:'))
a=int(input('digite o valor da moeda a:'))
b=int(input('digite o valor da moeda b:'))

cont=0


while cont<c:
    if c%a==0 or c%b==0:
        cont=cont+1
        print(cont)

    
        