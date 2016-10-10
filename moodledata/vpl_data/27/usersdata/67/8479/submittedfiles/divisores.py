# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input("Digite a quantidade de números que deve ser mostrada:")
a=input("Digite o número 1:")
b=input("Digite o número 2:")

i=1
j=1
while i<=n:
    
    if j%a==0 or j%b==0:
    print(j)
    i=i+1
j=j+1