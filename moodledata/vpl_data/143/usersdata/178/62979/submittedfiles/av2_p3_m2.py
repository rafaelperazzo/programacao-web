# -*- coding: utf-8 -*-

def degrau(c):
    nova=[]
    e=0
    for i in range(0,len(a)-1,1):
        e=c[i]-c[i+1]
        if e<0:
            e=e*(-1)
            nova.append(e)
    return(nova)
    
    
n=int(input('Digite o tamanho da sequência:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite os elementos da lista:'))
    a.append(valor)
    
print(degrau(c))
            
        
