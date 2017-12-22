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
        k = 0
        k = k + 1
        if lista[n - i] < lista[n - k]: 
            return 'S'
        else:
            return 'N'

def igualdade(lista):
    for i in range(0,n,1):
        if lista[0] == lista[1]:
            return 'S'
        elif lista[1] == lista[2]:
            return 'S'
        elif lista[2] == lista[3]:
            return 'S'
        elif lista[3] == lista[4]:
            return 'S'
        elif lista[4] == lista[5]:
            return 'S'
        elif lista[i] == lista[i + 1]:
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
    l2.append(int(input('digite o %d elemnto da lista2: ' % (1+i))))

for i in range (0,n,1):    
    l3.append(int(input('digite o %d elemnto da lista3: ' % (1+i))))

print (crescente1(l1))
print (decrescente(l1))
print (igualdade(l1))
print (crescente1(l2))
print (decrescente(l2))
print (igualdade(l2))
print (crescente1(l3))
print (decrescente(l3))
print (igualdade(l3))

    
    
    