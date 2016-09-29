# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
v=int(input('Digite a quantia em dinheiro: '))
x20=v//20
r20=v%20

x10=r20//10
r10=r20%10

x5=r10//5
r5=r10%5

x2=r5//2
r2=r5%2

x1=r2//1

print(x20)
print(x10)
print(x5)
print(x2)
print(x1)
    
