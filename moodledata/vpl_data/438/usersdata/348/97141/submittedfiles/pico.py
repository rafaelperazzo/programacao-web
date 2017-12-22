# -*- coding: utf-8 -*-
#funçoes
def crescente(lista):
    if n > 3:
        if (lista[0] < lista[1]) and (lista[1] > lista[2]):
            return 'N'
        if (lista[0] < lista[1]) and (lista[3] > lista[2]):
            return 'S'
        if (lista[i] < lista[i+1]) and (lista[n-2] < lista[n-1]):
            return'N'
    
    if n == 3:
        for i in range (n,-1,-1):    
            if lista[0] < lista[1] and lista[1] > lista[2]:
                return 'S'
            else:
                return 'N'
    

#codigo geral 
n = int(input('Digite a quantidade de elementos da lista: '))

l1 = []

for i in range (0,n,1):
    l1.append(int(input( 'informe o %d° elemento da lista: ' %(i+1))))
    
print(crescente(l1))    
  
    
    