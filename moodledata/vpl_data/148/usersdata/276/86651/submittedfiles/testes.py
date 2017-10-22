# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

A = int(input('Digite o dia 1: '))
B = int(input('Digite o mes 1: '))
C = int(input('Digite o ano 1: '))
D = int(input('Digite o dia 2: '))

if (A == B + C + D) and (B + C == D) and (B == C):
    print ('S')
else:
    print ('N')
