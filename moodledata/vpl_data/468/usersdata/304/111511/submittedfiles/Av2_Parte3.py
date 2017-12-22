# -*- coding: utf-8 -*-
m = int(input('Quantas listas: '))
n = int(input('Qntd elemento listas: '))

for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input('Elemento: ')))

media = sum(lista)/len(lista)
soma = sum(lista)*((lista[0]-media)**2)
dp = ((1/(n-1))*soma)**0.5

print(media)
print(dp)
