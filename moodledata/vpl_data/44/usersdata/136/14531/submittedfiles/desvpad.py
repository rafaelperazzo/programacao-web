# -*- coding: utf-8 -*-
from __future__ import division
import math

#comece abaixo

n = input("Digite n:")
a = []
for i in range (0, n, 1):
    a.append(input("Digite os valores:"))

i = 0
soma = 0
while i<n:
    soma = (soma + a[i])
    i = i+1
media = ((soma)/(len(a)))
print ("%.2f" %a[0])
print ("%.2f" %a[len(a) - 1])
print ("%.2f" %media)
print (a)

soma = 0
i = 0
for i in range (0, n, 1):
    soma = soma + (a[i]- media)**2
s = ((1/(n-1)) * soma)**0.5
print (s)