# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elemenetos em a: '))
m=int(input('Digite a quantidade de elemenetos em b: '))
a=[]
b=[]
cont=0
for i in range(0,n,1):
    valor_a=float(input('Digite o elemento de a: '))
    a.append(valor_a)
for i in range(0,m,1):
    valor_b=float(input('Digite o elemento de b: '))
    b.append(valor_b)
for i in range(0,m+1,1):
    if i in a and i in b:
        cont=cont+1
print(cont)

22,11,10,8,