# -*- coding: utf-8 -*-
A=int(input('digite o peso de A :'))
B=int(input('digite o peso de B :'))
C=int(input('digite o peso de C :'))
D=int(input('digite o peso de D :'))
if A==B+C+D and B+C==D and B==C:
    print('s')
else:
    print('n')

