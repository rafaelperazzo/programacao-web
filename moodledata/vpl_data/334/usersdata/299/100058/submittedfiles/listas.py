# -*- coding: utf-8 -*-
lista=[]
n=int(input(''))
for i in range(0,n,1):
    lista.append(int(input('')))
print(lista)    
listamodulos=[]
for i  in range(1,n,1):
    listamodulos.append(lista[i-1]-lista[i])
print(listamodulos)

for i in range(0,len(listamodulos)-1,1):
    if listamodulos[i]!<0:
        continue
    else:
        listamodulos[i]=listamodulos[i]*(-1)
print(listamodulos)    
    
    

