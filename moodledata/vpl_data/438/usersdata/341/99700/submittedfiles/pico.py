# -*- coding: utf-8 -*-

def pico(lista):
    y=[]
    n=len(lista)
    for i in range (0, n-1, 1):
        if (lista[i]<lista[i+1]):
            y.append(1)
        elif (lista[i]>lista[i+1]):
            y.append(2)
        else:
            y.append(0)
    c=sorted(y)        
    
    if (y==c):
        if(0 in y):
            print('N')
        elif (1 in y and 2 in y):
            print('S')
        else:
            print('N')
    else:
        print('N')
        
n = int(input('Digite a quantidade de elementos da lista: '))
lista=[]
for i in range (0,n,1):
    lista.append(int(input('Digite um elemento para o seu vetor: ')))
pico(lista)
