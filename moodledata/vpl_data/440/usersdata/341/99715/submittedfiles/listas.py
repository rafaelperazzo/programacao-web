# -*- coding: utf-8 -*-

n=int(input('Digite a quantidade de elementos de sua lista: '))
escada=[]
for x in range (0, n, 1):
    escada.append(int(input('Digite o %dº elemento de sua lista: ' %(x+1))))
degrau=[]
for y in range (0, n-1, 1):
    dif=escada[y+1]-escada[y]
    degrau.append(dif)
degrau=sorted(degrau)
i=len(degrau)-1
print(degrau[i])


