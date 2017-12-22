# -*- coding: utf-8 -*-
import numpy as np 
def Ldiferente (A,valordasoma):
    for i in range (0,n,1):
        soma=0
        for j in range (0,n,1):
            soma=soma + A[i,j]
        if valordasoma!= soma :
            return (i)
            
def Cdiferente (A,valordasoma):
    for j in range (0,n,1):
        soma=0
        for i in range (0,n,1):
            soma=soma + A[i,j]
        if valordasoma != soma:
            return (j)
            
def valordasoma (A) :
    a=0
    b=0
    c=0
    for i in range (0,n-2,1):
        for j in range (0,n,1):
            a=a+A[i,j]
            b=b+A[i+1,j]
            c=c+A[i+2,j]
        if a==b:
            return (a)
        if a==c:
            return (a)
        if b==c:
            return (b)
            
n=0

while n<3:
    n=int(input('dimensão da matriz'))
matriz=np.zeros((n,n))
for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i,j]=int(input('valor da posição %d%d' %(i+1,j+1)))
        
        
valor=valordasoma(matriz)
linha=Ldiferente(matriz,valor)
coluna=Cdiferente(matriz,valor)


soma=0
for i in range (0,n,1):
    soma=soma+matriz[linha,i]
erro=matriz[linha,coluna]
original=valor-(soma-erro)


print ('%d' %original)
print ('%d' %erro)
