# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

valor = int(input('Digite o valor: '))

c20 = valor//20
r20 = valor%20

c10 = r20//10
r10 = r20%10

c5 = r10//5
r5 = r10%5

c1 = r10

print (c20)
print (c10)
print (c5)
print (c1)