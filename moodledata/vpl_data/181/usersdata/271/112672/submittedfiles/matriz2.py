# -*- coding: utf-8 -*-
import numpy as np
#FUNÇÕES
def somalinha (A) :
    a=[]
    soma = 0
    for i in range (0,A.shape[0],1) :
        soma = 0
        for j in range (0,A.shape[1],1) :
            soma = soma + A[i,j]
        a.append(soma)
    return(a)
def somacoluna (A) :
    b = []
    soma = 0
    for j in range (0,A.shape[1],1) :
        soma = 0
        for i in range (0,A.shape[0],1) :
            soma = soma + A[i,j]
        b.append(soma)
    return(b)
    
def dprincipal (A) :

    soma = 0
    for i in range (0,A.shape[0],1) :
        soma = soma + A[i,i]
    return(soma)
        
def dsecundaria (A) :
    soma = 0
    for i in range (0,A.shape[0],1) :
        for j in range (0,A.shape[1],1) :
            if (i+j) == (A.shape[0]-1) :
                soma = soma + A[i,j]
    return(soma)
#ENTRADA
dimensao = int(input('Digite a dimensão da matriz: '))
z=np.zeros((dimensao,dimensao))

for i in range (0,dimensao,1) :
    for j in range (0,dimensao,1) :
        z[i,j] = int(input('Digite o elemento da matriz : '))
e = []
#PROCESSAMENTO
a  = (somalinha(z))
b = (somacoluna(z))
c = a + b 
c.append(dprincipal(z))
c.append(dsecundaria(z))

cont = 0

for i in range (0,len(c),1):
    if c[0] != c[i]:
        print('N')
        break
    else:
        cont = cont + 1 
    
if cont == (2*dimensao)+2 :
    print('S')


    
        
        
            
            


