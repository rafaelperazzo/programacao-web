# -*- coding: utf-8 -*-
p1=float(input('digite o peso da criança do lado esquerdo:'))
c1=float(input('digite o comprimento da gangorra do lado esquerdo:'))
p2=float(input('digite o peso da criança do lado direito:'))
c2=float(input('digite o comprimento da gangorra do lado direito:'))
if p1*c1==p2*c2:
    print('0')
elif p1*c1>p2*c2:
    print('-1')
else:
    if p2*c2>p1*c1:
        print('1')