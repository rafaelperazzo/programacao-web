# -*- coding: utf-8 -*-

def primeiralinha (A):
    for i in range (0,A,shape[0],1):
        for j in range (0, A.shape [1],1):
            if A[i,j]==1:
                return (i)
                
def ultimacoluna (A):
    for i in range (A.shape[0]-1,-1,-1):
        for j in range (A.shape[1]-1,-1,-1):
            if A[i,j]==1:
                return (i)
                
def primeiracoluna (A):
    for j in range (0,A.shape[1],1):
        for i in range (0,A.shape[0],1):
            if A[i,j]==1:
                return (j)

def ultimacoluna (A):
    for j in range(A.shape[1]-1,-1,-1):
        for i in range (A.shape[0],-1,-1):
            if A[i,j]==1:
                return (j)
                

linhas=int(input('número de linhas:'))
colunas=int(input('número de colunas:'))

A= np.zeros ((linhas,colunas))

for i in range(0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        A[i,j]=float(input('digite um elemento'))
        

menorlinha=primeiralinha(A)
maiorlinha=ultimalinha(A)
menorcoluna=primeiracoluna(A)
maiorcoluna=ultimacoluna(A)

B=A[menorlinha:maiorlinha+1 , menorcoluna:maiorcolina+1]
print(B)
