# -*- coding: utf-8 -*-

def pontomaximo(b):
    for i in range(0,len(b)-1,1):
        return(i)

def pico(b):
    m=pontomaximo(b)
    for i in range(m,len(b)-1,1):
        if b[i]<b[i+1]:
            return False
    return True
    
n=int(input('Digite a quantidade de termos:'))
a=[]
for i in range(0,n,1):
    valor=int(input('Digite os elementos da lista:'))
    a.append(valor)
    
if pico(a):
    
    
