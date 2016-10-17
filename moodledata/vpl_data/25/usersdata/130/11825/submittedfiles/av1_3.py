# -*- coding: utf-8 -*-
from __future__ import division
import math
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
cont=0
while True:
    cont=cont+1
    b=a%b
    a=b
    if a%b==0:
       break
print(b)
print(cont)
