# -*- coding: utf-8 -*-
A= int(input('A= '))
B= int(input('B= '))
C= int(input('C= '))
D= int(input('D= '))

if (A==B+C+D) and (B+C==D) and (B==C):
    print('S')
else:
    print('N')


