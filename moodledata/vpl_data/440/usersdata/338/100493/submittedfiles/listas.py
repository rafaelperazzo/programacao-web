# -*- coding: utf-8 -*-

n = int(input('Digite a quantidade de elementos de sua lista'))

escada = []
for k in range (0, n, 1):
    escada.append(int(input('Digite o %dº elemento de sua lista:' %(k+1))))

degrau=[]
for t in range (0, n, 1):
    dif=escada[t+1]-escada[t]
    degrau.append(dif)
    
degrau = sorted(degrau)
i = len(degrau)-1
print(degrau[i])

