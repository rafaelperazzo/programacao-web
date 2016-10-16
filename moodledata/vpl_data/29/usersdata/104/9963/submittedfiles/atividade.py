# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input('Digite o valor de n:')
i=1
cont=1
#PROCESSAMENTO
while i<=n:
    if n%i==0:
        cont=cont+1
    i=i*10
print(cont)


