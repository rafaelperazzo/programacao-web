# -*- coding: utf-8 -*-
n=int(input('digite o valor de n: '))
a=[]
soma1=0
soma2=0
c1=0
c2=0
for i in range (0,n,1):
    a.append(int(input('Digite o número: ')))
for i in range (0,n,1):
    if a[i]%2==0:
        soma1+=a[i]
    print(soma1)
    else:
        soma2+=a[i]
    print(soma2)

