# -*- coding: utf-8 -*-
def simpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+lista[i]
        b=soma
        return b
def spar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+lista[i]
        return soma
def qimpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==1:
            soma=soma+1
    return soma
def qpar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if lista[i]%2==0:
            soma=soma+1
    return soma
a=[]
n=int(input('quantidade:'))
for i in range(0,n,1):
    valor=float(input('número:'))
    a.append(valor)
print(simpar(a))
print(spar(a))
print(qimpar(a))
print(qpar(a))
        
        
        
        
        
        
        

