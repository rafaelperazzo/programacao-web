# -*- coding: utf-8 -*-
def iguais(a,b):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i] in b:
            cont=cont+1
    return cont
n1=int(input('Digite o tamanho da lista 1:'))
n2=int(input('Digite o tamanho da lista 2:'))
x=[]
y=[]
for i in range (0,n1,1):
    a=int(input('Digite um valor para lista 1:'))
    x.append(a)
for i in range (0,n2,1):
    b=int(input('Digite o tamanho da lista 2:'))
    y.append(b)
print(n1)
print(n2)
print(iguais(x,y))
