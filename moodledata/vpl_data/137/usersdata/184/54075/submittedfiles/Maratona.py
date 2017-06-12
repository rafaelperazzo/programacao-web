# -*- coding: utf-8 -*-
N=int(input('digite o número de postos de água:'))
M=int(input('digite a distância intermediária máxima do atleta:'))
p1=int(input('digite a posição em metros do posto de água:'))
p2=int(input('digite a posição em metros do posto de água:'))
p3=int(input('digite a posição em metros do posto de água:'))
total=p1+p2+p3
if total>=42.195:
    print('S')
else:
    print('N')