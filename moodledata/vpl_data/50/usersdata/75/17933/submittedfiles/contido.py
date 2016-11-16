# -*- coding: utf-8 -*-
from __future__ import division

def iguais(lista):
    cont=0
    for i in range (0,len(lista),1):
        if i==0:
            if lista[i]==lista[i]:
                cont=cont+1
            
        elif i==(len(lista)-1):
            if lista[len(lista)-1]==lista[len(lista)-1]:
                cont=cont+1
                
        else:
            if lista[i]==lista[i]:
                cont=cont+1
                
        cont=resultado
                
    
    if cont>0:
        return True
    else:
        return False
        
n=input('Digite a quantidade de termos da lista:')
m=input('Digite a quantidade de termos da lista:')

a=[]
b=[]

for i in range (0,n,1):
    a.append(input('Digite os valores da lista a:'))
    
for i in range (0,n,1):
    b.append(input('Digite os valores da lista b:'))
    
if iguais(a):
    print (resultado)
else:
    print (resultado)

                    
        

