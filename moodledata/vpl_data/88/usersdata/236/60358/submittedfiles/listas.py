# -*- coding: utf-8 -*-
def MAIORDEGRAU (A):
    maior=0
    DEGRAU=0
    for i in range (1,len(A),1):
        DEGRAU=abs(A[i-1]-A[i])
        
        if DEGRAU>maior:
            maior=DEGRAU
    print(maior)

N= int(input('Digite o número de termos da lista: '))
A=[]

for i in range (1,N+1,1):
    numero= int(input('n:'))
    A.append(numero)
    
MAIORDEGRAU(A)

