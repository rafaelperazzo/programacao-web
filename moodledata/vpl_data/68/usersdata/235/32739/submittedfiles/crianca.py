# -*- coding: utf-8 -*-
p1=float(input('digite o peso da criança da esquerda:'))
c1=float(input('digite o comprimento da esquerda:'))
p2=float(input('digite o o peso da criança da direita:'))
c2=float(input('digite o comprimento da direita:'))
if p1*c1==p2*c2:
    print('0')
elif p1*c1<p2*c2:
    print('1')
elif p1*c1==p2*c2:
    print('-1')