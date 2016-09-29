# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valor=int(input('Digite o valor: '))

n20=valor//20
n10=(valor%20)//10
n5=((valor%20)%10)//5
n2=(((valor%20)%10)%5)//2
n1=((((valor%20)%10)%5)%2)//1

print(n20)
print(n10)
print(n5)
print(n2)
print(n1)