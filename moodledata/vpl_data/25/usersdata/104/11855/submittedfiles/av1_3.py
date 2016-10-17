# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
cont=2
#PROCESSAMENTO+SAÍDA
if a<b:
    while b%a>0:
        cont=cont+1
        x=b%a
        b=a
        a=x
    print(a)
else:
    while a%b>0:
        cont=cont+1
        x=a%b
        a=b
        b=x
    print(b)
print(cont)
