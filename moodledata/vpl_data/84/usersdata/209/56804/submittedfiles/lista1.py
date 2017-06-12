# -*- coding: utf-8 -*-
def somaimpar(lista):
    soma=0
    for i in range(0,len(lista)-1,1):
        if a[i]%2==1:
            soma=soma+a[i]
    return soma
def somapar(lista):
    soma=0
    for i in range(0,len(lista)-1,1):
        if a[i]%2==0:
            soma=soma+a[i]
    return soma
def qtimpar(lista):
    soma=0
    for i in range(0,len(lista)-1,1):
        if a[i]%2==1:
            soma=soma+1
    return soma
def qtpar(lista):
    soma=0
    for i in range(0,len(lista)-1,1):
        if a[i]%2==0:
            soma=soma+1
    return soma
A=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(0,n,1):
    x=float(input('Digite um valor para a lista:'))
    A.append(x)
print(somaimpar(A))
print(somapar(A))
print(qtimpar(A))
print(qtpar(A))
print(A)

