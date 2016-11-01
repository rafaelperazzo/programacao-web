# -*- coding: utf-8 -*-
from __future__ import division
import math

l= input('Insira a quantidade de valores:')
F=[]
soma=0
for a in range (0,l,1):
    F.append(input('Insira um valor:'))
for i in range (0,l,1):
    soma= soma + F[i]
media= (soma/l)
s=0
for i in range (0,l,1):
    s= s + ((F[i]-media)**2)
dp=((1/(l-1))*s)**(1/2)
print('%.2f'%F[0])
print('%.2f'%F[l-1])
print('%.2f'%media)
print('%.2f'%dp)