# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor do primeiro número:')
b=input('Digite o valor do segundo número:')
#PROCESSAMENTO+SAÍDA
if a>b:
    for i in range(b,2,-1):
        if a%i==0 and b%i==0:
            print(i)
        
else:
    i=a
    while a%i!=0 and b%i!=0:
        i=i-1
    print(i)
        

