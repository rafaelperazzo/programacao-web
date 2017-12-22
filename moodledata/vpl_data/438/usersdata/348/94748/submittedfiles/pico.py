# -*- coding: utf-8 -*-
#funçoes
def crescente(lista):
    
    for i in range (0,n,1):
        if lista[0] > lista[1]:
            return 'N'
        elif (lista[0] < lita[1]) and (lista[3] > lista[2]):
            return 'N'
        elif (lista[0] < lista[1]) and (lista[1] > lista[2]):
            return 'S'
        elif lista[0] < lista[1]:
            return 'S' 
        
   
    

#codigo geral 
n = int(input('Digite a quantidade de elementos da lista: '))

l1 = []

for i in range (0,n,1):
    l1.append(int(input( 'informe o %d° elemento da lista: ' %(i+1))))
    
print(crescente(l1))    
    
    
    