# -*- coding: utf-8 -*-
def iguais(A,B):
    n=0
    m=0
    cont=0
    for m in range (0,M,1):
        for n in range (0,N,1):
            if B[m]==A[n]:
                cont=cont+1
    print(cont)    

N=int(input('Numero de elementos da primmeira lista:'))
M=int(input('Numero de elementos da segunda lista:'))

A=[]
B=[]

for i in range (1,N+1,1):
    numero= int(input('num:'))
    A.append(numero)
for i in range (1,M+1,1):
    numero= int(input('num:'))
    B.append(numero)

iguais (A,B)