# -*- coding: utf-8 -*-
import numpy as np
linhas=int(input('Informe o número de linhas:'))
colunas=int(input('Informe o número de colunas:'))
a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um elemento:'))

def quadrado_magico(a):
    lista=[]
    for i in range(len(a)):
        soma=0
        for j in range(len(a[i])):
            soma=soma+a[i,j]
    lista.append(soma)
    
    for i in range(len(a)):
        soma=0
        for j in range(len(a[i])):
            soma=soma+a[j,i]
    lista.append(soma)
    
    soma=0
    for i in range(len(a)):
        soma=soma+a[i,i]
    lista.append(soma)
    
    soma=0
    n=1
    for i in range(len(a)):
        soma=soma+a[i][len(a)-n]
        n=n+1
    lista.append(soma)
    
    for i in range(len(lista)):
        if lista[i]!=lista[1]:
            return False
        return True

if quadradro_magico(a):
    print('S')
else:
    print('N')
        
    

    
            
                    