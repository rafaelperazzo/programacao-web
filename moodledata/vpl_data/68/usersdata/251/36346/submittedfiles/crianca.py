# -*- coding: utf-8 -*-
p1 = int(input('Digite o peso da criança 1: '))
c1 = int(input('Digite o comprimento do lado da criança 1: '))
p2 = int(input('Digite o peso da criança 2: '))
c2= int(input('Digite o comprimento do lado da criança 2: '))
e1 = p1*c1
e2 = p2*c2

if e1>e2:
    print('-1')

elif e2>e1:
    print('1')
    
else:
    print('0')
