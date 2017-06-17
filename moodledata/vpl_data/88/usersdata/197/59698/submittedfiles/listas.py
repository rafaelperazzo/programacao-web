# -*- coding: utf-8 -*-
def degrau (a):
    b=[]
    for i in range (0,len(a)-1,1):
        diferenca=(-1)*(a[i]-a[i+1])
        b.append(diferenca)
    return (b)
def maior (a):
    maior=a[0]
    for i in range (0,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return (maior)
def maiordegrau (lista):
    b=degrau(lista)
    m=maior(b)
    return(m)
lista=[]
n=int(input('Digite o numero de elementos da lista:'))
for i in range (1,n+1,1):
    valor=float(input('Digite o numero da lista:'))
    lista.append(valor)
print(maiordegrau(lista))