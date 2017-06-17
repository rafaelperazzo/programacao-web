# -*- coding: utf-8 -*-
n=int(input('Informe o número de termos:'))
lista=[]
for i in range(0,n,1):
    numero=int(input('Digite um número:'))
    lista.append(numero)
    
def degrau(lista):
    lista2=[]
    for i in range(0,len(lista)-1,1):
        diferença=abs(lista[i]-lista[i+1])
        lista2.append(diferença)
    return (lista2)

def maior(lista):
    maior=lista[0]
    for i in range(0,len(lista),1):
        if lista[i]>maior:
            maior=lista[i]
    return(maior)
    
def maior_degrau(lista):
    lista2=degrau(lista)
    m=maior(lista2)
    return(m)
    
print(maior_degrau(lista))
       
    

