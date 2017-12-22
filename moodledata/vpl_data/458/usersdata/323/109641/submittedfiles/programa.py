# -*- coding: utf-8 -*-
import numpy as np
soma=0
pesos=[]
while True:
    n=int(input('Digite a dimensão do tabuleiro(n>=3): '))
    if n>=3:
        break
a=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        a[i,j]= int(input('Digite o elemento da matriz: '))
        
somalin=0
somacol=0

for i in range(0,n,1):
    for e in range(0,n,1):
        for j in range(0,n,1):
            somalin= somalin+ a[i,j]
            somacol=somacol+a[j,e]
        soma= somalin+somacol - 2*a[i,e]
        pesos.append(soma)
        somalin=0
        somacol=0
        soma=0
print((max(pesos)))