# -*- coding: utf-8 -*-
from __future__ import division

def pico(lista):
    
    posicao=0
    for i in range (0,len(lista)-1,1):
        if a[i]>a[i+1]:
            posicao = i
            break
    if posicao!=0:
        cont=0
        for i in range (posicao,len(lista)-1,1):
            if a[i] <= a[i+1]:
                cont=cont+1
        if cont == 0:
            return True
        else:
            return False
    else:
        return False
    
n = input('Digite a quantidade de elementos da lista: ')
a=[]

for i in range (0,n,1):
    a.append (input('Digite o valor de a:')):
        
        if pico(lista):
            print ('s')
        else:
            print ('N')

    
    
    
    
