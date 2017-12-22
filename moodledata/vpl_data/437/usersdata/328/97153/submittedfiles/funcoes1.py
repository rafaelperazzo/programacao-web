# -*- coding: utf-8 -*-
#escreva o código da função crescente aqui


def crescente (lista):
    som = 0
    for i in range (1,n,1):
        if lista[i]<=lista[i-1]:
            som+=1
    if som == 0:
        print('S')
    else:
        print('N')
    return 1


#escreva as demais funções
def lista(a):
    for i in range (0,n,1):
        a.append(int(input('Digite %a[%d]:' %(a,i))))
    return 1
    
    
    
    

def decrescente(lista):
    som = 0
    for i in range (1,n,1):
        if lista[i] >= lista [i-1]:
            soma = soma+1
    if som ==0:
        print('S')
    else:
        print('N')
    return 1

def iguais(lista):
    som = 0
    for i in range (0,n,1):
        for j in range (0,n,1):
            if i!=j:
                if lista[i]==lista[j]:
                    soma+=1
    if som == 0:
        print('N')
    else:
        print('S')
    return 1
    


#escreva o programa principal
n=int(input('tamanho da lista:'))
A = []
B = []
C = []

lista(A)
lista(B)
lista(C)

crescente(A)
decrescente(A)
iguais(A)
crescente(B)
decrescente(B)
iguais(B)
crescente(C)
decrescente(C)
iguais(C)






