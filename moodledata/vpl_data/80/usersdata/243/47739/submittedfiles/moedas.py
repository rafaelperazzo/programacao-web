# -*- coding: utf-8 -*-
from __future__ import division
c=int(input('digite o valor da cédula:'))
a=int(input('digite o valor da moeda a:'))
b=int(input('digite o valor da moeda b:'))

cont=0
i=1

while cont>0:
    if i%a==0 or i%b==0:
        cont=cont+1
        i=i+1
print(cont)        
    
        