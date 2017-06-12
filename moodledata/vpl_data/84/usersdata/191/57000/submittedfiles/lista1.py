# -*- coding: utf-8 -*-
def somaimpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+lista[i]
    return soma
def somapar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+lista[i]
    return soma
def qtimpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+1
    return soma
def qtpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+1
    return soma
D=[]
n=int(input('digite a quantidade de termos da lista:'))
for i in range(0,n,1):
    x=int(input('digite os valores da lista:'))
    D.append(x)
print(somaimpar(D))
print(somapar(D))
print(qtimpar(D))
print(qtpar(D))
print(D)

