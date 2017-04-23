# -*- coding: utf-8 -*-
p1=float(input('Digite o peso da criança do lado esquerdo:'))
c1=float(input('Digite o comprimento da gangorra do lado esquerdo:'))
p2=float(input('Digite o peso da criança do lado direito:'))
c2=float(input('Digite o comprimento da gangorra do lado direito:'))
l=p1*c1
l1=p2*c2
if (l>l1):
    print('-1')
elif (l1>l):
    print('1')
else:
    print('0')
