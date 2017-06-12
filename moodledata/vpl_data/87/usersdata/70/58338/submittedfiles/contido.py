# -*- coding: utf-8 -*-
def iguais(a,b):
    iguais=0
    for i in range(0, len(a), 1):
        for j in range(0, len(a), 1):
            if (d[i]==c[j]):
                iguais=iguais+1
    return(iguais)
    
n=int(input('Digite a quantidade de elementos da lista A: '))
m=int(input('Digite a quantidade de elementos da lista B: '))
a=[]
b=[]
for z in range (1, n+1, 1):
    valorA=int(input('Digite elementos da lista A: '))
    a.append(valorA)
for w in range (1, m+1, 1):
    valorB=int(input('Digite elementos da lista B: '))
    b.append(valorB)
print(iguais(a,b))
