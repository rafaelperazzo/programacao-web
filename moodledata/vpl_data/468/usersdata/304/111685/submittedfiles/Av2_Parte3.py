# -*- coding: utf-8 -*-
m = int(input('Quantas listas: '))
n = int(input('Qntd elemento listas: '))
for i in range (0,m,1):
    lista=[]
    for j in range (0,n,1):
        lista.append(int(input('Elemento: ')))
        
media = sum(lista)/len(lista)    
soma = 0
for i in range (0,(n-1),1):
    soma += ((i - media))
dp = ((1/(n-1))*(soma)**2)**(1/2)

print('%.2f'%media)
print('%.2f'%dp)
