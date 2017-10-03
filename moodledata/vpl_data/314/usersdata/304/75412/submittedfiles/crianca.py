# -*- coding: utf-8 -*-
p1 = float(input('Digite o peso 1: '))
c1 = float(input('Digite o comprimento 1: '))
p2 = float(input('Digite o peso 2: '))
c2 = float(input('Digite o comprimento 2: '))
if (p1*c1) == (p2*c2):
    print('0')
elif (p1*c1) > (p2*c2):
    print('-1')
else:
    print('1')