# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
#PROCESSAMENTO
if a>b:
    for i in range(b,n+b+1,1):
        if i%a==0 or i%b==0:
            print(i)
else:
    for i in range(a,n+a+1,1):
        if i%a==0 or i%b==0:
            print(i)
