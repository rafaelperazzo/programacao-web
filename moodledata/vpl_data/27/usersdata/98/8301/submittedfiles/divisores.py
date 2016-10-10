# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n: ')
a=input('Digite o valor de a: ')
b=input('Digite o valor de b: ')
i=1
contador=0

while True:
    if i%a==0 or i%b==0:
        print(i)
        contador=contador+1
    i=i+1
    if contador==n :
        break