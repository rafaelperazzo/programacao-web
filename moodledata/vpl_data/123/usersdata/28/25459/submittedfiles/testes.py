from __future__ import division
import numpy as np

def saem(a,k):
    cont = 0
    for i in range (0, a.shape[0], 1):
        if a[k,i] == 1: 
            cont = cont + 1
    return cont
    
def entram(a,k):
    cont = 0
    for i in range (0, shape[0]):
        if a[i,k] == 1:
            cont = cont + 1
    return cont
    
m = input('Digite o número de linhas: '))
n = int(input('Digite o número de colunas: '))

a = []

for i in range(0, m, 1):
    for j in range (0, n, 1):
        a.append(input('Digite um elemento para a matriz: ')
        
s = saem (a)
e = entram(a)

print (s)
print (e)