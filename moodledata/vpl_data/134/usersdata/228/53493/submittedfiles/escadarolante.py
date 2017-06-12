# -*- coding: utf-8 -*-
def rolagem(lista):
    for i in range (0,len(lista)-1,1):
        tempo=0
        if lista[i+1]<(lista[i]+10):
            tempo=tempo+(lista[i]-lista[i+1])
            
        elif lista[i+1]>=(lista[i]+10):
            tempo=tempo+10
        elif lista[len(lista-1)]<lista[len(lista)-2]+10:
            tempo=tempo+(lista[len(lista)-1]-lista[len(lista)-2])
        elif lista[len(lista)-1]>=lista[len(lista)-2]+10:
            tempo=tempo+10   
    return(tempo+10)        
    
n=int(input('digite um valor:'))
lista=[]
for i in range(0,n,1):
    tn=int(input('digite um tempo de passagem:'))
    lista.append(tn)
    

print (rolagem(lista))

            





