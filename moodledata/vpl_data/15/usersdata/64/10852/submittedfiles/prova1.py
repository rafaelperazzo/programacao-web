# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

print ("Os número tem que está entre 1 e 13")

a = int(input('Digite o valor da primeira carta: '))
b = int(input('Digite o valor da segunda carta: '))
c = int(input('Digite o valor da terceira carta: '))
d = int(input('Digite o valor da quarta carta: '))
e = int(input('Digite o valor da quinta carta: '))

if a>b>c>d>e:
    print ("D")
    if a<b<c<d<e:
        print("C")
else:
    print ("N")

