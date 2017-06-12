# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos:'
listaX=[]
listaY=[]
def media(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma1=soma1+lista[i]
    resultado=soma1/len(lista)
    return resultado
def DP(lista):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+(lista[i]-media(lista))**2
    DP=(soma2/(len(lista)-1))**(0.5)
    return (DP)
for i in range(0,n,1):
    num=float(input('Digite um valor:'))
    listaX.append(num)
for i in range(0,n,1):
    num=float(input('Digite um valor:'))
    listaY.append(num)
print('%.2f' %media(lista1))
print('%.2f' %DP(lista1))
print('%.2f' %media(lsita2))
print('%.2f' %DP(lista2))