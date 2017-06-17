# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos de a: ')) 
m=int(input('Digite a quantidade de elementos de b: '))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite os valores de a: '))
    a.append(valor)
b=[]
for i in range(0,m,1):
    y=int(input('Digite os valores de a: '))
    b.append(y)
def iguais(a,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont=cont+1
    return cont
print(iguais)