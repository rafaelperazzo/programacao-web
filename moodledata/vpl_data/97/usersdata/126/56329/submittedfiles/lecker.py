# -*- coding: utf-8 -*-


def lecker(a):
    if a[i]-1<a[i]>a[i]+1:
        return True
n=int(input('digite a quantidade de elementos da lista:'))
x=[]
y=[]
for i in range(0,n,1):
    p=float(input('digite o valor da lista 1:'))
    x.append(p)
    i=i+1
for i in range(0,n,1):
    q=float(input('digite o valor da segunda lista:'))
    y.append(q)
    i=i+1
if lecker(x):
    print('S')
else:print('N')
if lecker(y):
    print('S')
else:
    print('N')

    