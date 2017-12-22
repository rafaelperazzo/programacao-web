# -*- coding: utf-8 -*-
m = int(input('Quantas listas: '))
n = int(input('Qntd elemento listas: '))
for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input('Elemento: ')))
    
soma = 0
for i in range (0,(len(lista)-1),1):
    soma += (i - media)**2
media = sum(lista)/len(lista)
dp = ((1/(n-1))*soma)**0.5

print('%.2f'%media)
print('%.2f'%dp)
