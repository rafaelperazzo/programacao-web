# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=int(input('Digite um número:')
cont=1
i=1
#PROCESSAMENTO
while i<=n:
    if n%i!=0:
        cont=cont+1
    else:
        i=i*10
print(cont)


