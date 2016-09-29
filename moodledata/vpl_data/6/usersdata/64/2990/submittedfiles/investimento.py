# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA

vi = input('Digite o valor inicial: ')
t = input('Digite a taxa de crescimento percentual: ')

#PROCESSAMENTO

a = float(vi+(vi*t))
b = float(a+(vi*t))
c = float(b+(a*t))
d = float(c+(b*t))
e = float(d+(c*t))
f = float(e+(d*t))
g = float(f+(e*t))
h = float(g+(f*t))
i = float(h+(g*t))
j = float(i+(h*t))

#SAÍDA 

print ('%.2f' %(a))
print ('%.2f' %(b))
print ('%.2f' %(c))
print ('%.2f' %(d))
print ('%.2f' %(e))
print ('%.2f' %(f))
print ('%.2f' %(g))
print ('%.2f' %(h))
print ('%.2f' %(i))
print ('%.2f' %(j))
