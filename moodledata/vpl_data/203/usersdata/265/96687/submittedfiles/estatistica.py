# -*- coding: utf-8 -*-
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return(resultado)
def var(lista):
    somatorio=0
    for i in range(0,len(lista),1):
        somatorio=somatorio+(lista[i]-media)**2
    delta=(1/(n-1))*somatorio
    variancia=delta**(1/2)
    return(variancia)
n=int(input('digite a quantidade de termos da lista: '))
a=[]
b=[]
for i in range(0,n,1):
    valora=int(input('digite os termos da lista a: '))
    a.append(valora)
for i in range(0,n,1):
    valorb=int(input('digite os termos da lista b: '))
    a.append(valorb)
print('%.2f' %media(a))
print('%.2f' %var(a))
print('%.2f' %media(b))
print('%.2f' %var(b))