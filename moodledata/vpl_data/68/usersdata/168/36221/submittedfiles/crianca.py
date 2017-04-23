# -*- coding: utf-8 -*-
p1=float(input('Digite peso da criança do lado esquerdo: '))
p2=float(input('Digite peso da criança do lado direito: '))
c1=float(input('Digite o comprimento da gangorra do lado esquerdo: '))
c2=float(input('Digite o comprimento da gangorra do lado direito: '))
p1*c1==p2*c2
if (p1==p2) and (c1==p2):
    print('O')
elif (p1<p2) and (c1>c2):
    print('-1')
elif (p1>p2) and (c1<c2):
    print ('1')

