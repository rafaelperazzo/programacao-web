# -*- coding: utf-8 -*-
from funcoes1.py import crescente
def pico(lista):
    a=[]
    b=[]
    for i in range(0,len(lista),1):
        #analisar os elementos antes do pico
        if lista[i]<lista[i+1]:
            a.append(lista[i])
            continue
        else:
            b.append(lista[i])
            
    #analise crescente
    a.append(lista[i])
           
    #retorno caso a sequencia seja pico


l=[]
n = int(input('Digite a quantidade de elementos da lista: '))
for i  in range(0,n,1):
    l.append(int(input('')))
print(pico(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#CONTINUE...
