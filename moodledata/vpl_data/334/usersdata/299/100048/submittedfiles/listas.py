# -*- coding: utf-8 -*-
lista=[]
n=int(input(''))
for i in range(0,n,1):
    lista.append(int(input('')))
listamodulos=[]
for i  in range(1,n,0):
    listamodulos.append(lista[i-1]-lista[i])
for i in range(0,len(listamodulos)-1,1):
    if listamodulos[i]<0:
        listamodulos[i]*=-1
    else:
        continue
maior=0
for i in range(0,len(listamodulos)-1,1):
    for j in range(0,len(listamodulos)-1,1):
        if listamodulos[i]>=listamodulos[j]:
            maior=listamodulos[i]
        else:
            continue
print(maior)
    
    
    

