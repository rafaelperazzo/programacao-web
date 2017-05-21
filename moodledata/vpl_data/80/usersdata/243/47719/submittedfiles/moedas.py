# -*- coding: utf-8 -*-
from __future__ import division
c=int(input('digite o valor da cédula:'))
a=int(input('digite o valor da moeda a:'))
b=int(input('digite o valor da moeda b:'))

cont=0


while c>0:
    if c%a==0: 
        cont=cont+1
        c=c//a
       
    if c%b==0:
        cont=cont+1
        c=c//b
        
print(cont)        
    
        