# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite a dimensão da matriz:'))
a=np.zeros((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Informe um elemento da matriz:'))

def somalinha(a):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)    
    return(lista)

def somacoluna(a):
    l1=[]
    for i in range(0,a.shape[1],1):
        soma=0
        for j in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        l1.append(soma)    
    return(l1)    

def elemento(c):
    for i in range(0,len(c),1):
        cont=0
        for j in range(0,len(lista),1):
            if c[i]==c[j]:
                cont=cont+1
        if cont==1:
            return (i)
def numero(lista,termo):
    for i in range(0,len(lista),1):
        if i!=termo:
            numero=lista[termo]-lista[i]
            return (numero)

lista=somalinha(a)
l1=somacoluna(a)
x=elemento(lista)
y=elemento(l1)
z=a[x,y]
w=z-(numero(lista,x))

print('%d'%w)
print('%d' %z)

            
    
    
    
        


