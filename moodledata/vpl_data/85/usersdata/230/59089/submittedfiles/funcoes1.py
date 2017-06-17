# -*- coding: utf-8 -*-

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
        if cont==(len(lista)-1):
            return(True)
        else:
            return(False)

#escreva as demais funções
def decrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
        if cont==(len(lista)-1):
            return(True)
        else:
            return(False)

def iguais(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
        return False


#escreva o programa principal
n=int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(1,n+1,1):
    valor=int(input('Digite elementos da lista1: '))
    a.append(valor)
    
b=[]
for i in range(1,n+1,1):
    valor2=int(input('Digite elementos da lista2: '))
    b.append(valor2)
    
c=[]
for i in range(1,n+1,1):
    valor3=int(input('Digite elementos da lista3: '))
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


if crescente(c):
    print('S')
else:
    print('N')
if decrescente(c):
    print('S')
else:
    print('N')
if iguais(c):
    print('S')
else:
    print('N')


