# -*- coding: utf-8 -*-
import numpy as np
d= int(input('Digite o tamanho da matriz:'))
l= int(input('Digite a linha da matriz:'))
c= int(input('Digite a coluna da matriz:'))

h=np.zeros((d,d))

for i in range (0,d,1):
    for j in range (0,d,1):
        h[i,j]= int(input('Digite o elemento da matriz:'))
        
def soma_l(t,indice_l):
    soma=0
    for j in range (0,t.shape[1],1):
        soma= soma+t[indice_l,j]
    return (soma)
    
def soma_c(v,indice_c):
    soma=0
    for i in range (0,v.shape[0],1):
        soma= soma+v[i,indice_c]
    return (soma)
    
result= soma_l(h,l)+soma_c(h,c)-(2*h[l,c])

print ('%d' %result)