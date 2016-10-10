# -*- coding: utf-8 -*-
from __future__ import division
import math

n1= int(input('Digite o primeiro valor: ')
n2= int(input('Digite o segundo valor: ')

if n1<n2:
    i=n1
else:
    i=n2
while True:
    if n1%1==0 and n2%i==0:
        print(i)
        break