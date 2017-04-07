# -*- coding: utf-8 -*-
import math
f=float(input('digite um valor para f:'))
l=float(input('digite um valor para l:'))
q=float(input('digite um valor para q:'))
H=float(input('digite um valor para variação de altura:'))
O=float(input('digite um valor para O:'))
g=9.81
e=0.00002
D=((8*f*l*(q**q))**(0.5))/((math.pi*g*H)**(0.5))
Rey=(4*q)/(math.pi*D*O)
k=(0.25)/(math.log10(e/(3.7*D)+(5.74/(Rey**0.9)))**2)
print('o valor de D é: %.4f'%D)
print('o valor de Rey é: %.4f'%Rey)
print('o valor de k é: %.4f'%k)