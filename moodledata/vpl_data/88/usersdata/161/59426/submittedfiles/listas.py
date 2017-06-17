# -*- coding: utf-8 -*-
n=int(input('Informe o número de termos:'))
lista=[]
for i in range(0,n,1):
    numero=int(input('Digite um número:'))
    lista.append(numero)
    
def degrau(lista):
    for i in range(1,len(lista),1):
       degrau=lista[i]-lista[i+1]
       return (degrau)
print(degrau)
       
    

