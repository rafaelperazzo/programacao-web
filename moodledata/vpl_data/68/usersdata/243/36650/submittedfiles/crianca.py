# -*- coding: utf-8 -*-
pl=float(input('dig o peso da cri1:'))
c1=float(input('dig o compr1:'))
p2=float(input('dig o peso da cri2:'))
c2=float(input('dig o compr2:'))

fator1=p1*c1
fator2=p2*c2

if fator1==fator2:
    print('0')
if fator1>fator2:
    print('-1')
if fator1<fator2:
    print('1')

