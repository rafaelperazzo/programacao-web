# -*- coding: utf-8 -*-
from __future__ import division
import math
n=input('Digite a quantidade de multiplos:')
a=int(input('Digite o primeiro numero:'))
b=int(input('Digite o segundo numero:'))
c=0
i=2
while c<n:
    if i%a==0 or i%b==0:
        print (i)
        c=c+1
    i=i+1
    