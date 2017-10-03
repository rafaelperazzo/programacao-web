# -*- coding: utf-8 -*-
p1 = float(input('Digite o peso da criança no lado esquerdo: '))
p2 = float(input('Digite o peso da criança no lado direitoo: '))
c1 = float(input('Digite o comprimento da gangorra no lado esquerdo: '))
c2 = float(input('Digite o comprimento da gangorra no lado direito: '))

if p1*c1 == p2*c2:
    print('0')
elif p1*c1>p2*c2:
    print('-1')
else:
    print('1')


