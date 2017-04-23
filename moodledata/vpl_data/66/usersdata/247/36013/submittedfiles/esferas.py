# -*- coding: utf-8 -*-
A=float(input('digite o peso da esfera 1'))
B=float(input('digite o peso da esfera 2'))
C=float(input('digite o peso da esfera 3'))
D=float(input('digite o peso da esfera 4'))
if A==B+C+D and D==B+C and B==C:
    print('S')
else:
    print('N')