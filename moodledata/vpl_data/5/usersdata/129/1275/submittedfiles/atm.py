# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
A= int(input('Digite o valor a ser sacado: '))
B= (A//20)
C= (A%20)//10
D= ((A%20)%10)//5
E= (((A%20)%10)%5)//2
F= ((((A%20)%10)%5)%2)//1
print B
print C
print D
print E
print F
