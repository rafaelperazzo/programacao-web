# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite a:')
b=input('Digite b:')
c=input('Digite c:')
ka=0
kb=0
contador=0

while ka<=c//a:
    kb=(c-ka*a)//b
    if ka*a+kb*b==c:
        contador=contador+1
        
    else:
        ka=ka+1
if contador>0:
    print (ka)
    print (kb)
else:
    print ('n')