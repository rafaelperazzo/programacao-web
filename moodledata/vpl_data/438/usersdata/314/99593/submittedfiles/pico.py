# -*- coding: utf-8 -*-

def pico(lista):
    crescente=True
    decrescente=True
    maior=lista[0]
    for i in range(1,len(lista)-1,1):
        if lista[i]>maior:
            maior=lista[i]
            crescente=True
            
        else:
            crescente=False
            break
    
    for j in range(i+1,len(lista)-1,1):    
        if maior>lista[i+1]:
            decrescente=True        
        else:
            decrescente=False
            break
    if crescente and decrescente:
        print("'S'")
    else:
        print("'N'")
    if lista[0]==maior:
        print("'N'")
        
        

        
    





n=int(input('Digite n: '))
lista=[]
for i in range(0,n,1):
    lista.append(int(input('Digite a quantidade de elementos da lista: ')))

pico(lista)    

