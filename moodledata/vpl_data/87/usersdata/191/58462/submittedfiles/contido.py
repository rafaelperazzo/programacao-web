# -*- coding: utf-8 -*-
def iguais(a,b):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i] in b:
            cont=cont+1
    return cont
n1=int(input('tamanho lista 1:'))
n2=int(input('tamanho lista 2:'))
A=[]
B=[]
for i in range(0,n1,1):
    a=int(input('valor lista 1:'))
    A.append(a)
for i in range(0,n2,1):
    b=int(input('valor lista 2:'))
    B.append(b)
print(n1)
print(n2)
print(iguais(A,B))



