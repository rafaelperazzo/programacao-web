# -*- coding: utf-8 -*-

n=int(input('digite o valor de n:'))
lista=[]
for i in range(0,n,1):
    numero=int(input('digite o valor de n:'))
    lista.append(numero)
    
def degrau(lista):
    l=[]
    for i in range(0,len(lista)-1,1):
        diferença=abs(lista[i]-lista[i+1])
        l.append(diferença)
        return(l)
        
print(degrau(lista))        