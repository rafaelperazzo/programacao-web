# -*- coding: utf-8 -*-
from __future__ import division
import math

n=int(input('Digite o valor de n:'))

a=1
soma=0 
for a in range (1,n+1,1):
        J=a/(a**2)
        if a%2==0:
            soma= soma-J
        else: soma=soma+J
print('%.5f' %soma)
a=a+1    