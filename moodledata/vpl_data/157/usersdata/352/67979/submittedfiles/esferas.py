# -*- coding: utf-8 -*-


A=float(input('Digite o 1 peso:'))
B=float(input('Digite o 2 peso:'))
C=float(input('Digite o 3 peso:'))
D=float(input('Digite o 4 peso:'))

if (A==B+C+D) and (B+C==D) and (B==C):
    print('S')
else: 
    print('N')