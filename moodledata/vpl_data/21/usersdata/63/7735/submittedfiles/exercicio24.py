# -*- coding: utf-8 -*-
from __future__ import division
import math

a=int(input('Digite o valor de a:'))
b=int(input('Digite o valor de b:'))
contador=100
i=1

if a<b:
    if b%a==0:
        print (a)
if b<a:
    if a%b==0:
        print(b)

while i<a and i<b:
    if a%i==0 and b%i==0:
        contador=contador-1
        print (contador)
    
    

    