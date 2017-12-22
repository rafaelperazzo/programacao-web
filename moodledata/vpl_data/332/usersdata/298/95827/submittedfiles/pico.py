# -*- coding: utf-8 -*-

def pico(lista):
    for i in range (0, len(lista)-1, 1):
        if lista[i]==lista[i+1]:
            pico=False
    
    for i in range (0, len(lista)-1, 1):
        if lista[i]<lista[i+1]:
            continue
        if lista[i]>lista[i+1]:
            k1=lista[i]
            jj=lista.index(lista[i])
            break
    for u in range (len(lista)-1, 0, -1):
        if lista[u]<lista[u-1]:
            continue
        if lista[u]>lista[u-1]:
            k2=lista[u]
            jh=lista.index(lista[u])
            break
    if k1==k2 and jj==jh:
        pico=True
    if not k1==k2:
        pico=False
    return pico
    


n = int(input('Digite a quantidade de elementos da lista: '))
lista=[]
for i in range (0, n, 1):
    lista.append(int(input('Adicione um elemento à lista: ')))

if pico(lista)==False:
    print('N')
if pico(lista)==True:
    print('S')











