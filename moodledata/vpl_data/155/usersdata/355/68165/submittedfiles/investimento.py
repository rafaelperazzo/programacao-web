# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA
d = float(input('Digite o valor do investimento inicial: '))
p = float(input('Digite a taxa de crescimento percentual: '))
#PROCESSAMENTO
i = d+(p*d)
j = i+(p*i)
k = j+(p*j)
l = k+(p*k)
m = l+(p*l)
n = m+(p*m)
o = n+(p*n)
q = o+(p*o)
r = q+(p*q)
s = r+(p*r)
print(i)
