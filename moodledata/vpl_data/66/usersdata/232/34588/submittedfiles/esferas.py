# -*- coding: utf-8 -*-
A=float(input('Digite o valor da esfera 1: '))
B=float(input('Digite o valor da esfera 2: '))
C=float(input('Digite o valor da esfera 3: '))
D=float(input('Digite o valor da esfera 4: '))
if A==B+C+D and B+C==D and B==C:
    print('S')
else:
    print('N')
