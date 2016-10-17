# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
cont=0
#PROCESSAMENTO+SAÍDA
if a<b:
    if b%a==0:
        print(a)
        cont=1
    else:
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
        if a%b==0:
            cont=cont+1
    print(b)
print(cont)
