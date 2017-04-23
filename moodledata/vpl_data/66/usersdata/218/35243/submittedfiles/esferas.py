# -*- coding: utf-8 -*-
A=float(input('digite o peso da esfera A:'))
B=float(input('digite o peso da esfera B:'))
C=float(input('digite o peso da esfera C:'))
D=float(input('digite o peso da esfera D:'))
if A==B+C+D:
    if B+C==D:
        if B==C:
            print('S')
else:
    print('N')