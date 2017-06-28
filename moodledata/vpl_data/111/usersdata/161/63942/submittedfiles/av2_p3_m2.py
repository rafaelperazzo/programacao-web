# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite a dimensão da matriz:'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Informe um elemento da matriz:'))

def somalinha(a):
    soma=0
    l=[]
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        l.append(soma)    
    return(soma)
somal=somalinha(a)

def somacoluna(a):
    soma=0
    l1=[]
    for i in range(0,a.shape[1],1):
        for j in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        l1.append(soma)    
    return(soma)    
somac=somacoluna(a)

def igual(a):
    for i in range(0,len(lista),1):
        cont=0
        for j in range(0,len(lista),1):
            if lista[i]==lista[j]:
                cont=cont+1
        if cont>=2:
            return (i)
def diferença(a):
    for i in range(0,len(lista),1):
        cont=0
        for j in range(0,len(lista),1):
            if lista[i]==lista[j]:
                cont=cont+1
        if cont==1:
            return(i)

l=diferença(somal)
l1=diferença(somac)
resultado=a[l,l1]-(diferença(somal)-igual(somal))
print('%d'%resultado)
print('%d' %a[l,l1])

            
    
    
    
        


