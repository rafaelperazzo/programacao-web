# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CODIGO AQUI

n= int(input('Digite o total de notas: '))

N20 = int(n / 20)
N10 = int((n - (N20*20))/10)
N5 = int(int((n - (N10*10) - (N20*20))/5))
N2 = int((n - (N10*10) - (N20*20) - (N5*5))/2)
N1 = int((n - (N10*10) - (N20*20) - (N5*5) - (N2*2)))

print (N20)
print (N10)
print (N5)
print (N2)
print (N1)


