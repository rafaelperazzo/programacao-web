# -*- coding: utf-8 -*-
A=int(input('Digite o peso da esfera A: '))
B=int(input('Digite o peso da esfera B: '))
C=int(input('Digite o peso da esfera C: '))
D=int(input('Digite o peso da esfera D: '))
if A==B+C+D:
    if B+C==D:
        if B==C:
            print('S')
else:
    print('N')
    

