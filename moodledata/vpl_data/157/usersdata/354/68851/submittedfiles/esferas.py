# -*- coding: utf-8 -*-
A=int(input('Digite o valor de A: '))
B=int(input('Digite o valor de B: '))
C=int(input('Digite o valor de C: '))
D=int(input('Digite o valor de D: '))
#PROCESSAMENTO
if A==B+C+D and B+C==D and B==C:
    print('S')
else:
    print('N')
