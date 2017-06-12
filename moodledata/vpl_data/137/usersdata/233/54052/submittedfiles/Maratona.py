# -*- coding: utf-8 -*-
N=int(input('N: '))
M=int(input('M: '))
anterior=0
a=int(input('a: '))
diferença=a-anterior
cont=0
for i in range(1,N,1):
    anterior=a
    a=int(input('a: '))
    diferença=a-anterior
    if diferença>M:
        cont=cont+1
if cont>0:
    print('N')
else:
    print('S')