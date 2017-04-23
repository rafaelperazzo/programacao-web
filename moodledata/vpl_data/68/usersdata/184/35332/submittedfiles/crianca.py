# -*- coding: utf-8 -*-
p1=float(input('digite o peso da criança do lado esquerdo:'))
c1=float(input('digite o comprimento da gangorra do lado esquerdo:'))
p2=float(input('digite o peso da criança do lado direito:'))
c2=float(input('digite o comprimento da gangorra do lado direito:'))
lado esquerdo= p1*c1
lado direito= p2*c2
if lado esquerdo==lado direito and c1>c2:
    print('zero')
    print('menos um')
elif lado esquerdo==lado direito and c2>c1:
    print('zero')
    print('um')


