# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return True
    else:
        return False


#escreva as demais funções
def descrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
        if cont==(len(lista)-1):
            return True
        else:
            return False
            
def iguais(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
    return False
    





#escreva o programa principal

n=int(input('digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    valor1=int(input('digite o elemento da lista 1:'))
    a.append(valor1)
    
b=[]
for i in range(1,n+1,1):
    valor2=int(input('digite o elemento da lista 2:'))
    b.append(valor2)
    
c=[]
for i in range(1,n+1,1):
    valor3=int(input('digite os elementos da lista 3:'))
    c.append(valor3)

if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if iguais(a):
    print('S')
else:
    print('N')
    
if crescente(b):
    print('S')
else:
    print('N')
if decrescente(b):
    print('S')
else:
    print('N')
if iguais(b):
    print('S')
else:
    print('N')
