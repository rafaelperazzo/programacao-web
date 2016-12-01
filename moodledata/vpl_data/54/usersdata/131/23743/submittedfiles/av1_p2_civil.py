# -*- coding: utf-8 -*-
from __future__ import division

#entrada
m=input('altura do pino:')
n=input('quantidade de pinos:')
#código 
i=1
lista=[]
while i<=n:
    lista.append(input('tamanho do pino:'))
    i=i+1
j=0
cont=0

while j<(n-1):
    while lista[j]>m and lista[j+1]>m:
        lista[j]=lista[j]-1
        lista[j+1]=lista[j+1]-1
        cont=conta+1
    while lista[j]<m and lista<m:
        lista[j]=lista[j]+1
        lista[j+1]=lista[j+1]+1
        cont=cont+1
    while lista[j]>m:
        lista[j]=lista[j]-1
        cont=cont+1
    while lista[j]<m:
        lista[j]=lista[j]+1
        cont=cont+1
    j=j+1
    
if lista[j]!=m:
    while lista[j]>m:
        lista[j]=lista[j]-1
        cont=cont+1
    while lista[j]<m:
        lista[j]=lista[j]+1
        cont=cont+1
        
print cont
print lista
            
        
    
