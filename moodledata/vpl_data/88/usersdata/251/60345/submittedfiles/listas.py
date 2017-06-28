# -*- coding: utf-8 -*-
def degrau(lista):
    degraus=[]
    iten=0
    for i in range(1,len(lista),1):
        iten=abs(lista[i]-lista[i-1])
        degraus.append(iten)
    maiorDegrau=max(degraus)
    return(maiorDegrau)
    
lista=[]
n=int(input('Digite a quantidade de termos da lista: '))

for i in range (0,n,1):
    elemento=float(input('Digite o valor do termo de índice '+str(i)+' da lista: '))
    lista.append(elemento)

print(('%d')%degrau(lista))    
