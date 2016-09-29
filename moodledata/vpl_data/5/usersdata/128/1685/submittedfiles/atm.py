# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

valor=int(input('Digite o valor a ser sacado: '))

n20=valor//20
print n20

n10=(valor-(n20*20))//10
print n10

n5=(valor-((n20*20)+(n10*10)))//5
print n5

n2=(valor-((n20*20)+(n10*10)+(n5*5)))//2
print n2

n1=(valor-((n20*20)+(n10*10)+(n5*5)+(n2*2)))
print n1