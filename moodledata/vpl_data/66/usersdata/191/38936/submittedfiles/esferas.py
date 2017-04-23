# -*- coding: utf-8 -*-
A=float(input('digite o peso da esfera A:'))
B=float(input('digite o peso da esfera B:'))
C=float(input('digite o peso da esferaC:'))
D=float(input('digite o peso da esfera D:'))
if A==B+C+D and B+C==D and B==C:
    print('S')
else:
    print('N')


