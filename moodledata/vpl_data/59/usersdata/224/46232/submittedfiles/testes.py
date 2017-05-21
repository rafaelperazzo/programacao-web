# -*- coding: utf-8 -*-
p1=float(input('Digite o valor p1: '))
p2=float(input('Digite o valor p2: '))  
c1=float(input('Digite o valor c1: '))  
c2=float(input('Digite o valor c2: '))  
if p1*c1==p2*c2:
    print('0')
if p1*c1>p2*c2:
    print('-1')
if p1*c1<p2*c2:
    print('1')