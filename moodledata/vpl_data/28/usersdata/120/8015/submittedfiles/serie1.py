# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
s=i/(i*2)
n=int(input('insira o valor de n:'))
#PROCESSAMENTO
soma=0
for i in range (1,n+1,1):
    soma= soma+(s*((-1)^(i+1)))
print soma   
   
