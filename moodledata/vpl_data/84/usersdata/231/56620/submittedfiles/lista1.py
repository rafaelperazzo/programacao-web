# -*- coding: utf-8 -*-
def s.impar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if len(i)%2==1:
            soma=soma+len(i)
        return soma
def s.par(lista):
    soma=0
    for i in range(0,len(lista),1):
        if len(i)%2==0:
            soma=soma+len(i)
        return soma
def q.impar(lista):
    soma=0
    for i in range(0,len(lista),1):
        if len(i)%2==1:
            soma=soma+1
    return soma
def q.par(lista):
    soma=0
    for i in range(0,len(lista),1):
        if len(i)%2==0:
            soma=soma+1
    return soma
a=[]
n=int(input('quantidade:'))
for i in range(0,n,1):
    valor=float(input('número:'))
    a.append(valor)
print(s.impar)
        
        
        
        
        
        
        

