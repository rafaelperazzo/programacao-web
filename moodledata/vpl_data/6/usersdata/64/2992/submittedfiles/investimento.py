# -*- coding: utf-8 -*-
from __future__ import division

#ENTRADA

vi = input('Digite o valor inicial: ')
t = input('Digite a taxa de crescimento percentual: ')

#PROCESSAMENTO

a = float(vi+(vi*t))
b = float(a+(a*t))
c = float(b+(b*t))
d = float(c+(c*t))
e = float(d+(d*t))
f = float(e+(e*t))
g = float(f+(f*t))
h = float(g+(g*t))
i = float(h+(h*t))
j = float(i+(i*t))

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
