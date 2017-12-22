# -*- coding: utf-8 -*-

def crescente (lista1,lista,lista3):
    #escreva o código da função crescente aqui
    for i in range (0,n,1):
        if lista1[i]<(lista1[i+1]):
            return True
        if lista1[i]>=(lista1[i+1]):
            return False
   
    for i in range (0,n,1):
        if lista2[i]<(lista2[i+1]):
            return True
        if lista2[i]>=(lista2[i+1]):
            return False
   
    for i in range (0,n,1):
        if lista3[i]<(lista3[i+1]):
            return True
        if lista3[i]>=(lista3[i+1]):
            return False

#escreva as demais funções
def decrescente (lista1,lista,lista3):
    for i in range (0,n,1):
        if lista1[i]>=(lista1[i+1]):
            return True
        if lista1[i]<(lista1[i+1]):
            return False
   
    for i in range (0,n,1):
        if lista2[i]>=(lista2[i+1]):
            return True
        if lista2[i]<(lista2[i+1]):
            return False
   
    for i in range (0,n,1):
        if lista3[i]>=(lista3[i+1]):
            return True
        if lista3[i]<(lista3[i+1]):
            return False




#escreva o programa principal
n=int(input('Digite a quantidade de elementos das tres listas: '))
lista1=[]
for i in range (0,n,1):
    lista1.append(int(input('Digite um valor %d para a lista_1: '%(i+1))))
lista2=[]
for i in range (0,n,1):
    lista2.append(int(input('Digite um valor %d para a lista_2: '%(i+1))))
lista3=[]
for i in range (0,n,1):
    lista3.append(int(input('Digite um valor %d para a lista_3: '%(i+1))))
if crescente (lista1,lista2,lista3):
    print ('S')
else:
    print ('N')
if decrescente (lista1,lista2,lista3):
    print ('S')
else:
    print ('N')

