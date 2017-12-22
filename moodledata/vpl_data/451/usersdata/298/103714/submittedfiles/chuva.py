# -*- coding: utf-8 -*-
n=int(input('Digite o numero de seçoes da piscina: '))
alturas=[]
for i in range (0, n, 1):
    alturas.append(int(input('Digite a atura da seçao %d: ' % (i+1))))

cont=0
for i in range (1, n-1, 1):
    if alturas[i-1]>=alturas[i]<alturas[i+1] or alturas[i-1]>=alturas[i]<=alturas[i+1]:
        cont+=1

print(cont)