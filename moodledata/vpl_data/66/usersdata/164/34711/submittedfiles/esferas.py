# -*- coding: utf-8 -*-
A=float(input('Digite A: '))
B=float(input('Digite B: '))
C=float(input('Digite C: '))
D=float(input('Digite D: '))
if (B==C) and (A==B+C+D):
    A=B+C+D
    D=B+C
    print('S')
else:
    print('N')

