# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
cont=0
c=a%b
while True:
    cont=cont+1
    if a%b==0:
        print(b)
        break
    a=b and b=c
print(cont)        

      