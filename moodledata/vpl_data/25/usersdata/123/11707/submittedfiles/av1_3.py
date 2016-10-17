# -*- coding: utf-8 -*-
from __future__ import division
import math
l= int(input('Insira um número:'))
f= int(input('Insira um número:'))
if (l>f):
    maior=l
    menor=f
elif (f>l):
    maior=f
    menor=l
cont=0
while True:
    MDC=(maior%menor)
    maior=menor
    menor=MDC
    cont=cont+1
    if ((maior%menor)==0):
        break
print (MDC)
print (cont)