# -*- coding: utf-8 -*-

p1=float(input('digte o peso da criança do lado esquerdo:'))
c1=float(input('digte o comprimento do lado esquerdo:'))
p2=float(input('digte o peso da criança do lado direito:'))
c2=float(input('digte o comprimento do lado direito:'))
if (p1*c1)>(p2*c2):
    print('-1')
elif (p1*c1)<(p2*c2):
    print('1')
else:    
    print('0')