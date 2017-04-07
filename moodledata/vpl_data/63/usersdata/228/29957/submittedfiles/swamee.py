# -*- coding: utf-8 -*-
import math
f=float(input('digite um valor para f:'))
l=float(input('digite um valor para l:'))
q=float(input('digite um valor para q:'))
H=float(input('digite um valor para variação de altura:'))
v=float(input('digite um valor para v:'))
g=9.81
e=0.000002
D=(8*f*l*(q*q))**(0.20)/(((math.pi**2)*g*H))**(0.2)
Rey=(4*q)/(math.pi*D*v)
k=(0.25)/((math.log10((e/(3.7*D))+(5.74/(Rey**(0.9)))))**2)
print('o valor de D é: %.4f'%D)
print('o valor de Rey é: %.4f'%Rey)
print('o valor de k é: %.4f'%k)