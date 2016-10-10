# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n:')
a=input('Digite o valor de a:')
b=input('Digite o valor de b:')
#PROCESSAMENTO
x=1
while x<=n:
    if x==1:
        x=x+1
    elif x%a==0 or x%b==0:
        print(x)
x=x+1

