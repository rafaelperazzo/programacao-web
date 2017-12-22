# -*- coding: utf-8 -*-
m=(int(input()))
n=(int(input()))
desvio=0
matriz=[]
for i in range(0,m,1) :
    lista=[]
    for j in range (0,n,1) :
      lista.append(int(input()))
    matriz.append(lista[i])  
media=[]
total=[]
desvio=[]
soma=0
for i in range(0,m,1):
    media.append(sum(matriz[i])/n)
    
    
    
    
    
    
    
    
while(True):
    i=0
    
    for j in range(0,n,1) :
        
     desvio=desvio+((matriz[i][j]-media[i])**2/(len(matriz[i])-1.0))
     i=i+1
     if i==m:
        break
    
    total.append(desvio)
for i in range (0,m,1):
    print(media[i])
    print(desvio**0.5)















































