# -*- coding: utf-8 -*-
A=float(input('digite o valor A:'))
B=float(input('digite o valor B:'))
C=float(input('digite o valor C:'))
D=float(input('digite o valor D:'))
if A<=B and A<=C and A<=D:
    print(A)
    if B>=C and B>=D:
        print(B)
    elif C>=B and C>=D:
        print(C)