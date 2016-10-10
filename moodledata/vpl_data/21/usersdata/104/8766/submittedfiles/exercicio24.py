# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor do primeiro número:')
b=input('Digite o valor do segundo número:')
#PROCESSAMENTO+SAÍDA
if a>b:
    i=b
    while i>=1:
        if a%i==0 and b%i==0:
            print(i)
            break
        else:
            i=i-1
            
        
        
else:
    i=a
    while i>=1:
        if a%i==0 and b%i==0:
            print(i)
            break
        else:
            i=i-1
        

