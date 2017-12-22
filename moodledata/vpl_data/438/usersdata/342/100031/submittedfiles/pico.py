# -*- coding: utf-8 -*-

def pico(lista):
    a = []
    n = len(lista)
    for i in range (0,n-1,1):
        if (lista[i] < lista[i+1]):
            a.append(i)
        elif (lista[i] > lista[i+1]):
            a.append (2)
        else:
            a.append(0)
            
    x = sorted (a)
    
    if (a==x):
        if (0 in a):
            print ('N')
        elif (1 in a and 2 in a):
            print ('S')
    else:
        print ('N')
    
    

n = int(input('Digite a quantidade de elementos da lista: '))
lista = []
for i in range (0,n,1) :
    lista.append(int(input('Insira os elemetos da lista: ')))

