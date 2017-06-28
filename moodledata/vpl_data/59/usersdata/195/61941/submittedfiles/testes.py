# -*- coding: utf-8 -*-
def pico(x):
    a=(len(x)+1)//2
    b=a-1
    for i in range(1,a,1):
        if x[i]<x[i-1]:
            return False
    return True
n=int(input('digite o tamanho da lista:'))
x=[]
for i in range(1,n+1,1):
    a=int(input('digite a:'))
    x.append(a)
cont=0
for i in range(1,len(x),1):
    if x[i]==x[i-1]:
        cont=cont+1
if cont==0:
    if pico(x):
        print('S')
    else:
        print('N')
else:
    print('N')