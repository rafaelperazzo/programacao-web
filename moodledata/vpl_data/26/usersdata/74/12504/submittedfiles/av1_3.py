# -*- coding: utf-8 -*-
from __future__ import division
import math

n = input('Digite o valor inteiro: ')
r = input('Digite o valor real: ')

cont = 1
cont2 = 0
i = 1
j = 10
k = 1/10
l = 1
m = 0

while n>=i:
    if n/j>=1:
        cont = cont +1
    j = j*10
    i = i+1
print('%d'% cont)
while r>=k:
    m = m+1
    l = l*10
    k = k*(1/l)
    n = (r*l)-r
    r = -(n/l-r)
print('%d'% m)
    

