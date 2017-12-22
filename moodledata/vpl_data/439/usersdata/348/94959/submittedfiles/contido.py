# -*- coding: utf-8 -*-
#funçao 
def intersercao(l1,l2):
    return set (l1).intersection(l2)





#codigo geral 
n = int(input( 'informe na quantidade de elementos de n: '))
m = int(input( 'informe a quantidade de elementos de m: '))

l1 = []
l2 = []

for i in range (0,n,1):
    l1.append(int(input('informe o %d° elemento da lista1: ' %(i+1))))
for i in range (0,m,1):
    l2.append(int(input('informe o %d° elemento da lista2: ' %(i+1))))

print(intersercao(l1,l2))
    
    

