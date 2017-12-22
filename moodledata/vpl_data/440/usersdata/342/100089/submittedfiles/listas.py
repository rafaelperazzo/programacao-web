# -*- coding: utf-8 -*-
n = int(input('insira a quantidade de elementos da lista:'))

escada = []
for a in range (0,n,1):
    escada.append(int(input('digite o %d° elemento da lista:' %(k+1))))
    
deg = []
for b in range (0,n-1,1):
    dif = escada[b+1]-escada[b]
    deg.append(dif)
    
ded = sorted(deg)
i = len(deg)-1
print(deg[i])
    

