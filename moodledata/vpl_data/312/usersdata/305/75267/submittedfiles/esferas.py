# -*- coding: utf-8 -*-
A = int(input('digite o valor de A: '))
B = int(input('digite o valor de B: '))
C = int(input('digite o valor de C: '))
D = int(input('digite o valor de D: '))
if A == B + C + D and D == C + B and B == C:
    print('S')
else:
    print('N')

