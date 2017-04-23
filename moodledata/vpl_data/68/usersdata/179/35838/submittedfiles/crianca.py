# -*- coding: utf-8 -*-
p1=float(input('peso da esquerda'))
c1=float(input('comprimento da esquerda'))
p2=float(input('peso da direita'))
c2=float(input('comprimento da direita'))
if p1*c1==p2*c2:
    print('0')
elif p1*c1>p2*c2:
    print('-1')
else :
    print('1')


