# -*- coding: utf-8 -*-


def lecker(a):
    i=0
    cont=0
    for i in range(0,len(a),1):
        if a[i]>a[i]+1 0r or a[i]<a[i]+1>a[i]+2 or a[len(a)]>a[len(a)-1]:
            cont=cont+1
    if cont>0:
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

    