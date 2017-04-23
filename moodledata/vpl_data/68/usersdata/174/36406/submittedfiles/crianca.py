# -*- coding: utf-8 -*-
p1 = float(input('Peso 1:'))
c1 = float(input('Comprimento 1:'))
p2 = float(input('Peso 2:'))
c2 = float(input('Comprimento 2:'))
if (p1*c1)==(p2*c2):
    print('0')
elif (p1*c1)>=(p2*c2):
    print('-1')
else:
    print('1')

