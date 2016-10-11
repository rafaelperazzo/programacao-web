# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=int(input("Digite o valor de n: "))
contador=0
#PROCESSAMENTO
while n>0:
    n=n//10
    contador=contador+1
print contador
    