# -*- coding: utf-8 -*-

def pico(lista):
    x = []
    n=len(lista)
    for i in range (0,n-1,1):
        if (lista[i] < lista[i+1]):
            x.append(i)
        elif (lista[i] > lista[i+1]):
            x.append (2)
        else:
            x.append(0)
            
    a = sorted (x)
    
    if (x==a):
        if (0 in x ):
            print ('N')
        elif (1 in x and 2 in x):
            print ('S')
        else:
            print ('N')
    else:
        print ('N')
    
    

n = int(input('Digite a quantidade de elementos da lista: '))
lista = []
for i in range (0,n,1) :
    lista.append(int(input('Insira os elemetos da lista: ')))
    
pico(lista)

