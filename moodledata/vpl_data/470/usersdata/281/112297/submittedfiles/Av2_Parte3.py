# -*- coding: utf-8 -*-
m=int(input('Digite a quantidade de listas desejada: '))
lista=[]
for i in range(0,m,1):
    n=int(input('Digite a quantidade de elementos da %d lista: ' %(i+1)))
    for i in range(0,n,1):
        lista.append(int(input('Digite o %d elemento dessa lista: ' %(i+1))))
    media=sum(lista)/len(lista)
    print(media)
    
    
        
        

