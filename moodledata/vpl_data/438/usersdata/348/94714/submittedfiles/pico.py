# -*- coding: utf-8 -*-
#funçoes
def crescente(lista):
    
    while i <= n:
        i = 0
        if lista[i] < lista[i+1] and lista[n] > lista[n-1]:
            return 'S'
        i = i +1
   
    

#codigo geral 
n = int(input('Digite a quantidade de elementos da lista: '))

l1 = []

for i in range (0,n,1):
    l1.append(int(input( 'informe o %d° elemento da lista: ' %(i+1))))
    
print(crescente(l1))    
    
    
    