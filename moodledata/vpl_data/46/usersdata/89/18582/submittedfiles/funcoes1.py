# -*- coding: utf-8 -*-
from __future__ import division

def crescente (lista):
   contador=0
   for i in range(0,len(lista),1):
       if i==0:
           if lista[0]<lista[1]:
               contador=contador+1
        elif i=(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                contador=contador+1
        else:
            if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
                contador=contador+1
    
    if contador==len(lista):
        return True
    else:
        return False


#escreva as demais funções
def decrescente(lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
           if lista[0]>lista[1]:
               contador=contador+1
        elif i=(len(lista)-1):
            if lista[len(lista)-1]<lista[len(lista)-2]:
                contador=contador+1
        else:
            if lista[i]<lista[i-1] and lista[i]>lista[i+1]:
                contador=contador+1
    
    if contador==len(lista):
        return True
    else:
        return False

def consecutivosiguais(lista):
    contador=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]==lista[1]:
                contador=contador+1
                
        elif i==(len(lista)-1):
            if lista[len(lista)-1]==lista[len(lista)-2]:
                contador=contador+1
        else:
            if lista[i]==lista[i-1] and lista[i]==lista[i+1]:
                contador=contador+1
    
    if contador!=0:
        return True
    else:
        return False
        
#escreva o programa principal
a=[]
b=[]
c=[]

n=input('digite a quantidade de elementos da lista a:')
