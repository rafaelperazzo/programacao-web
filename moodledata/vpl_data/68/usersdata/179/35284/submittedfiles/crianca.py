# -*- coding: utf-8 -*-
p1=float(input('peso da esquerda'))
c1=float(input('comprimento da esquerda'))
p2=float(input('peso da direita'))
c2=float(input('comprimento da direita'))
GA1=p1*c1
GA2=p2*c2
if GA1==GA2:
    print('0')
elif GA1>GA2:
    print('-1')
elif GA2>GA1:
    print('1')

