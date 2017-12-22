# -*- coding: utf-8 -*-
m=(int(input()))
n=(int(input()))
desvio=0
matriz=[]
for i in range(0,m,1) :
    lista=[]
    for j in range (0,n,1) :
      lista[i].append(int(input()))
    matriz.apppend(lista)  
media=[]
total=[]
for i in range(0,m,1):
    media.append(sum(media[i])/len(media[i]))
while(True):
    i=0
    desvio=[]
    for j in range(0,n,1) :
        
     desvio=desvio+((matriz[i][j]-media[i])**2/(len(matriz[i])-1.0))
     i=i+1
     if i==m:
        break
    
    total.append(desvio)
for i in range (0,m,1):
    print(media[i])
    print(desvio**0.5)















































