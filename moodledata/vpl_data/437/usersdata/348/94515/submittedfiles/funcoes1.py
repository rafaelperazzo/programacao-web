# -*- coding: utf-8 -*-

#escreva o código da função crescente aqui
def crescente1(lista):
    for i in range (0,n,1):
        if lista[i] < lista[i+1]:
            return 'S'
        else:
            return 'N'
  
        
#escreva as demais funções
def decrescente(lista):
    for i in range (0,n,1):
        if lista[i] > lista[i+1]:
            return 'S'
        else:
            return 'N'

def igualdade(lista):
    for i in range(0,n,1):
        if lista[i] == lista[i+1]:
            return 'S'
        else:
            return 'N'

       
#escreva o programa principal

n = int(input('informe a quantidade de elementos: '))

l1 = []
l2 = []
l3 = []

for i in range (0,n,1):
    l1.append(int(input('digite o %d elemnto da lista1: ' % (1+i))))
for i in range (0,n,1):   
    l2.append(int(input('digite o %d elemnto da lista1: ' % (1+i))))
for i in range (0,n,1):    
    l3.append(int(input('digite o %d elemnto da lista1: ' % (1+i))))

print(crescente1(l1)


    
    
    