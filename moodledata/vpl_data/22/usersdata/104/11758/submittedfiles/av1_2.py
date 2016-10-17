# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
x=input('Digite o código:')
#PROCESSAMENTO+SAÍDA
a=x//1000
b=(x%1000)//100
c=((x%1000)%100)//10
d=((x%1000)%100)%10
if a!=b and a==c and b!=d:
    print('V')
elif a!=b and a!=c and b==d:
    print('V')
else:
    print('F')

