# -*- coding: utf-8 -*-
from __future__ import division
import math

n= input('Digite o valor de n: ')
a=[]

for i in range(0,n,1):
    a.append(input('Digite o número: '))
s=0
for i in range(0,n,1):
    s=s+a[i]
