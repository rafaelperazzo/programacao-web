# -*- coding: utf-8 -*-
n=int(input('Digite a ordem da matriz: '))
a=[]
for i in range (n):
    b=[]
    for j in range(n):
        b.append(int(input('Digite o valor: ')))
    a.append(b)
    
#Função que define a diagonal dominante
def diagonal(lista):
    for i in range(0,(len(lista)),1):
        if lista[i][i]>(sum(lista[i])-lista[i][i]):
            return print('S')
        else:
            return print('N')
            
diagonal(a)
            

    
