# -*- coding: utf-8 -*-

def pico(lista):
    maior=lista[0]
    for i in range(0,len(lista)-1,1):
        if lista[i]>maior:
            maior=lista[i]
            crescente=True
    meio=lista.index(lista[i])
        if meio>lista[i]:
            decrescente=True        
        else:
            decrescente=False
            crescente=False
            
        
    





n=int(input('Digite n: '))
lista=[]
for i in range(0,n,1):
    lista.append(int(input('Digite a quantidade de elementos da lista: ')))

