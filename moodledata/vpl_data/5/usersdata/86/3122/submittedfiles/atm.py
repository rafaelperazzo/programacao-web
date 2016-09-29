# -*- coding: utf-8 -*-
from __future__ import division
import math

#entrada
v = int(input('digite o valor em reais:'))
#processamento
n20 = v//20
n10 = (v%20)//10
n5 = (v-(v%20)//10))//5
n2 = (v-((v%20)//10)//5))//2
n1 = (v-(((v%20)//10)//5)//2))//1

#saida
print(n20)
print(n10)
print(n5)
print(n2)
print(n1)

