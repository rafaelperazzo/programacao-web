# -*- coding: utf-8 -*-
#####################################################################
def crescente (lista):
    crescente = 0
    for i in range(1, len(lista)):
        if lista[i]>lista[i-1]:
            crescente += 1
    if crescente == len(lista):
        return 'S'
    else:
        return 'N'
#####################################################################
def decrescente(lista):
    decrescente = 0
    for i in range(1, len(lista)):
        if lista[i]<lista[i-1]:
            decrescente += 1
    if decrescente == len(lista):
        return 'S'
    else:
        return 'N'
#####################################################################
def iguais(lista):
    iguais = False
    for i in range(1, len(lista)):
        if lista[i]== lista[i-1]:
            iguais = True
            break
    if iguais:
        return 'S'
    else:
        return 'N'
#####################################################################
def recebeVetor(qntItens):
    vetor = []    
    for i in range(0, qntItens):
        vetor.append(int(input('Insira o valor %d: ' % (i+1))))
    return vetor
a = [0, 0, 0]

n= int(input('Quantidade de dados: '))
for i in range (0, 3):
    a[i]= recebeVetor(n) 

for i in range (0, 3):
    print(crescente(a[i]))
    print(decrescente(a[i]))
    print(iguais(a[i]))
    
    
        
        
        
        
        
        