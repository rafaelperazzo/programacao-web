# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input("Digite o valor de n:"))
contador=0
i=1
while (n>0):
    if n//10!=0:
        contador=contador+1
        i=i+1
    print(contador)