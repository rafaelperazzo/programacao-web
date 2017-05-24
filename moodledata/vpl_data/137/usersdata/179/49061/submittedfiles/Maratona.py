# -*- coding: utf-8 -*-
N=int(input('digite o valor de N :'))
M=int(input('digite o valor de M :'))
dt=42195
for i in range(0,dt+1,1):
    N1=int(input('digite o valor de N1 :'))
    if N1>=M:
        print('S')
    elif N1<M:
        print('N')