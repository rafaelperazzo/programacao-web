# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI
valorSacado=int(input('digite o valor a ser sacado:'))


n20=valorSacado//20
a=valorSacado-(n20*20)
n10=a//10
b=a-(n10*10)
n5=b//5
c=b-(n5*5)
n2=c//2
d=c-(n2*2)
n1=d


print(n20)
print(n10)
print(n5)
print(n2)
print(n1)
