# -*- coding: utf-8 -*-
import math
f=int(input('digite um valor para f:'))
l=int(input('digite um valor para l:'))
q=int(input('digite um valor para q:'))
H=int(input('digite um valor para variação de altura:'))
O=int(input('digite um valor para O:'))
g=9.81
e=0.00002
D=((8*f*l*(q*q))**(0.20))/(((math.pi**2)*g*H)**(0.20))
Rey=(4*q)/(math.pi*D*O)
k=(0.25)/(math.log10((e)/(3.7*D))+(5.74)/(Rey**0.9)**2)
print('o valor de D é: %.4f'%D)
print('o valor de Rey é: %.4f'%Rey)
print('o valor de k é: %.4f'%k)