# -*- coding: utf-8 -*-

p1 = float(input('Digite o peso da crianca do lado esquerdo: '))
c1 = float(input('Digite o comprimento do lado esquerdo da gangorra: '))
p2 = float(input('Digite o peso da crianca do lado direito: '))
c2 = float(input('Digite o comprimento do lado direito da gangorra: '))

if (p1*c1 == p2*c2):
    print ('0')
elif (p1*c1 > p2*c2):
    print ('-1')
elif (p1*c1 < p2*c2):
    print ('1')

