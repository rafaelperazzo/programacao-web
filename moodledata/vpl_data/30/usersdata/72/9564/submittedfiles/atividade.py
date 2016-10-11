# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=int(input('digite o valor de n:'))
if n<=0:
    n=n*(-1)
i=1
soma=0
#PROCESSAMENTO
while i<=n:
    soma=soma+(i)/(n-(i-1))
    i=i+1
    
#SAIDA
print soma
    
    
    
    