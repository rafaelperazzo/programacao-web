# -*- coding: utf-8 -*-
import math
A=int(input('Digite o valor de A:'))
B=int(input('Digite o valor de B:'))
C=int(input('Digite o valor de C:'))
D=int(input('Digite o valor de D:'))
if A>B:
    if C>B and C>D or D>C:
        print('N')
    else:
        print('S')
elif B>A and B>C:
    