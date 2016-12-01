# -*- coding: utf-8 -*-
from __future__ import division

def modulo(c):
   modulo=((c**2)**0.5)
   return modulo
   
    
def maior(lista):
   maior=lista[0]
   for i in range (0,len(lista),1):
       if lista[i]>maior:
           maior=lista[i]
   
   return maior 

def menor(lista):
    menor=lista[0]
    for i in range (0,len(lista)-1,1):
        if lista[i]<menor:
            menor=lista[i]
            
    return menor  
    
def variacao(lista,m):
    a=maior(lista)
    b=menor(lista)
    x=modulo(a-m)
    y=modulo(b-m)
    
    z=x+y
    
    return z
        

lista=[]
n=input('diga a quantidade de pinos:')
m=input('diga a altura:')

for i in range(0,n,1):
    lista.append(input('diga o valor do pino:'))
    
r=variacao(lista,m)
print ('%d' %r)