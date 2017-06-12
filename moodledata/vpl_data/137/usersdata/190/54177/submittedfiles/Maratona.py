# -*- coding: utf-8 -*-
N=int(input('N:'))
M=int(input('M:'))
ant=0
a=int(input('digite a:'))
dif=a-ant
cont=o
for i in range(1,N,1):
    ant=a
    a=int(input('digite a: '))
    dif=a-ant
    if dif>M:
        cont=cont+1
if cont>0:
    print('N')
else:
    print('S')
    