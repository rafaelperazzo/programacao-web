# -*- coding: utf-8 -*-
def iguais(c,d):
    cont=0
    j=0
    for i in range (0, len(d), 1):
        if (d[i]==c[j]):
            cont=cont+1
        j=j+1    
    return(iguais)
    
n=int(input('Digite a quantidade de elementos da lista A: '))
m=int(input('Digite a quantidade de elementos da lista B: '))
a=[]
b=[]
for z in range (1, n+1, 1):
    valorA=int(input('Digite os elementos da lista A: '))
    a.append(valorA)
print(iguais(a,b))    
    
for w in range (1, m+1, 1):
    valorB=int(input('Digite os elementos da lista B: '))
    b.append(valorB)
print(iguais(b,a))    
