# -*- coding: utf-8 -*-
p1=float(input('digite o peso da pessoa do lado esquerdo:'))
c1=float(input('digite o comprimento do lado esquerdo:'))
p2=float(input('digite o peso da pessoa do lado direito:'))
c2=float(input('digite o comprimento do lado direito:'))
if p1*c1==p2*c2:
    print('0')
if p1*c1>p2*c2:
    print('-1')
if p1*c1<p2*c2:
    print('+1')

