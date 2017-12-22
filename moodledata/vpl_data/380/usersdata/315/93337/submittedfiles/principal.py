# -*- coding: utf-8 -*-
import random
#COMECE AQUI ABAIXO
x = []
n = int(input('digite n: '))
Dn = 0
for i in range(0,n,1):
    x.append ( int(input('digite valor: ')))
    Dn+= 1.0/x[i]
MH = n/Dn
print (MH)
    














