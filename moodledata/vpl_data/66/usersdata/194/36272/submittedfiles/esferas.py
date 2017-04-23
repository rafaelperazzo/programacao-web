# -*- coding: utf-8 -*-
A=int(input('Digite o valor de A:'))
B=int(input('Digite o valor de B:'))
C=int(input('Digite o valor de C:'))
D=int(input('Digite o valor de D:'))
if A==B+C+D and B+C==D and B==C:
    print('s')
else:
    print('n')
