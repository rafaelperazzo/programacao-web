# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

c = int(input('Digite o valor a ser sacado: '))

c1 = (c//20)
c2 = (c%20)//10
c3 = ((c%20)%10)//5
c4 = (((c%20)%10)%5)//2
c5 = ((((c%20)%10)%5)%2)//1

print ('%d' %c1)
print ('%d' %c2)
print ('%d' %c3)
print ('%d' %c4)
print ('%d' %c5)
