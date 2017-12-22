# -*- coding: utf-8 -*-
m = int(input('Quantas listas: '))
n = int(input('Qntd elemento listas: '))
matriz = []
for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input('Elemento: ')))
    matriz.append(lista)
    
soma = 0
for i in range (0,(len(lista)-1),1):
    soma += i
media = sum(lista)/len(lista)
dp = ((1/(n-1))*soma*((lista[0]-media)**2))**0.5

print('%.2f'%media)
print('%.2f'%dp)
