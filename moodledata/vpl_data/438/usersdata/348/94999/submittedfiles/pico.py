# -*- coding: utf-8 -*-
#funçoes
def crescente(lista):
    
    

    for i in range (n,-1,-1):    
        if lista[0] > lista[1]:
            return 'N'
        elif (lista[i-1] < lista[i-2]) and (lista[0] < lista[1]) :
            return 'S'
        elif (lista[0] < lista[1]): 
            return 'S'
        elif lista[0] < lista[1]:
            return 'S' 
        i = i+1
def crescente1(lista):
    if lista[2] lista[3]:
        return'N'
    

#codigo geral 
n = int(input('Digite a quantidade de elementos da lista: '))

l1 = []

for i in range (0,n,1):
    l1.append(int(input( 'informe o %d° elemento da lista: ' %(i+1))))
    
print(crescente(l1))    
print(crescente(l1))    
    
    