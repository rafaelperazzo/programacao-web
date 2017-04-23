# -*- coding: utf-8 -*-
import math
A=int(input('digite o comprimento do lado A:'))
B=int(input('digite o comprimento do lado B:'))
C=int(input('digite o comprimento do lado C:'))
if A>=B and B>=C:
    print('S')
    if (A*A)==(B*B)+(C*C):
        print('Re')
    elif (A*A)>(B*B)+(C*C):
        print('Ob')
    else:
        print('Ac')
if A==B and B==C:
    print('Eq')
elif A!=B and B!=C:
    print('Es')
else:
    print('Is')
else:
    print('N')