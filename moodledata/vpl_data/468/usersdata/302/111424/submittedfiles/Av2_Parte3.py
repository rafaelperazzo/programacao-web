# -*- coding: utf-8 -*-

m = int(input('Digite a quantidade de listas: '))
n = int(input('Digite o número de elementos das listas: '))
i = 1
while(i <= m):
    lista = []
    for j in range(n):
        lista.append(float(input('Digite o elemento %d da lista %d: ' %((j+1),(i+1)))))
    i += 1
for i in range(m):
    media = sum(lista)/len(lista)
    print(media)
        
