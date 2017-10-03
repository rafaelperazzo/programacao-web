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

print(1ºano:%.2f'%i)
print(2ºano:%.2f'%j)
print(3ºano:%.2f'%k)
print(4ºano:%.2f'%l)
print(5ºano:%.2f'%m)
print(6ºano:%.2f'%n)
print(7ºano:%.2f'%o)
print(8ºano:%.2f'%q)
print(9ºano:%.2f'%r)
print(10ºano:%.2f'%s)