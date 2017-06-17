# -*- coding: utf-8 -*-
def degrau(b):
    degrau=0
    for j in range (0, len(b), 1):
        if (b[j]>b[j+1]):
            degrau=b[j]-b[j+1]
        else:
            degrau=b[j+1]-b[j]
            
n=int(input('Digite o número de elementos da lista: '))
a=[]
for i in range (1, n+1, 1):
    valor=int(input('Digite os elementos da lista: '))
    a.append(valor)
print(degrau(a))    
