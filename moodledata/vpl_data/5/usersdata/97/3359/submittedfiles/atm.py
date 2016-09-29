# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
n=int(input('Digite um valor:'))

a1=(n//20)
a2=(n%20)//10
a3=((n%20)%10)//5
a4=(((n%20)%10)%5)//2
a5=((((n%20)%10)%5)%2)//1

print('%d'%a1)
print('%d'%a2)
print('%d'%a3)
print('%d'%a4)
print('%d'%a5)



