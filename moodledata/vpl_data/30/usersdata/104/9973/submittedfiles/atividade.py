# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n:')
s=0
#PROCESSAMENTO
if n<0:
    n=-n
for i in range(1,n+1,1):
    s=s+(i)/(n+1-i)
#SAÍDA
print(s)
    