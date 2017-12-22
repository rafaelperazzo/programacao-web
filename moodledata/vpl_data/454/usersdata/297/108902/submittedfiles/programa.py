# -*- coding: utf-8 -*-
c=int(input('digite o numero de elementos da lista: '))
estoque=[]
lista=[]
for i in range(c):
    estoque.append(int(input()))
for i in range(0,c,1):
    if estoque[i] not in lista:
        lista.append(estoque[i])
total=len(lista)*2
print(int(total))
    
