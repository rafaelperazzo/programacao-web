# -*- coding: utf-8 -*-
n=int(input('digite: '))
m=int(input('digite: '))
nt=0
cont=0
for i in range(0,n-1,1):
    nx=int(input('digite: '))
    nt=nx-nt
    if nt<=m:
        cont=cont+0
    if nt>m:
        cont=cont+1
if cont==0:
    print('S')
else:
    print('N')