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
    a=a*i
    b=b*i
    i=i+1
    contador=contador+2
    print a
    print b