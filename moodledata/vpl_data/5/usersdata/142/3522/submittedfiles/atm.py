# -*- coding: utf-8 -*-
from __future__ import division
import math

V = input('Digite o valor a ser sacado:')

C20 = V//20
C10 = (V%20)//10
C5 = ((V%20)%10)//5
C2 = (((V%20)%10)%5)//2
C1 = ((((V%20)%10)%5)%2)//1

print (C20)
print (C10)
print (C5)
print (C2)
print (C1)