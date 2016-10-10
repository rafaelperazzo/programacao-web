# -*- coding: utf-8 -*-
from __future__ import division
import math
#ENTRADA
n=input("Digite o valor de n: ")
a=input("Digite o valor de a: ")
b=input("Digite o valor de b: ")
i=1
contador=0
#PROCESSAMENTO
while contador<=n:
    if a*i!=b*i:
        contador=contador+i
        c=a*i
        d=b*i
        print c
        print d
    else:
        contador=contador+1
    i=i+1