# -*- coding: utf-8 -*-
quantidade=int(input("Digite a quantidade de termos na lista: "))
lista=[]
for i in range(0,quantidade,1):
    lista.append(float(input("Digite o termo: ")))


soma=0    
for termo in range(0,len(lista)-1,1):
    degrau=lista[termo]-lista[termo+1]
    while