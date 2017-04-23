# -*- coding: utf-8 -*-
p1=float(input('Digite o peso do lado esquerdo: '))
c1=float(input('Digite o comprimento do lado esquerdo: '))
p2=float(input('Digite o peso do lado direito: '))
p2=float(input('Digite o comprimento do lado direito: '))
if(p1*c1)>(p2*c2):
    print('-1')
elif((p1*c1)<(p2*c2)):
    print('1')
else:
    print('0')