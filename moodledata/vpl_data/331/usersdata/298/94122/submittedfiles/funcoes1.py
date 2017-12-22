# -*- coding: utf-8 -*-

def crescente (lista):
    k=0
    for i in range (0, len(lista)-2, 1):
        if lista[i]<lista[i+1]:
            k+=0
        if lista[i]>=lista[i+1]:
            k+=1
    if k==0:
        cresc=True
    if not k==0:
        cresc=False
    return cresc


#escreva as demais funções
def decrescente (lista):    
    k=0
    for i in range (0, len(lista)-2, 1):
        if lista[i]>lista[i+1]:
            k+=0
        if lista[i]<=lista[i+1]:
            k+=1
    if k==0:
        decresc=True
    if not k==0:
        decresc=False
    return decresc

def elem_iguais (lista):    
    k=0
    for i in range (0, len(lista)-2, 1):
        if not lista[i]==lista[i+1]:
            k+=0
        if lista[i]==lista[i+1]:
            k+=1
    if k==0:
        iguais=False
    if not k==0:
        iguais=True
    return iguais

#escreva o programa principal

n=int(input('Digite o número de elementos das listas: '))

lista1=[]
for i in range (0, n, 1):
    lista1.append(int(input('Digite o elemento %d da lista 1: ' % (i+1))))

lista2=[]
for i in range (0, n, 1):
    lista2.append(int(input('Digite o elemento %d da lista 2: ' % (i+1))))

lista3=[]
for i in range (0, n, 1):
    lista3.append(int(input('Digite o elemento %d da lista 3: ' % (i+1))))

if crescente (lista1)==True:
    print('S')
else:
    print('N')
if decrescente (lista1)==True:
    print('S')
else:
    print('N')
if elem_iguais (lista1)==True:
    print('S')
else:
    print('N')

if crescente (lista2)==True:
    print('S')
else:
    print('N')
if decrescente (lista2)==True:
    print('S')
else:
    print('N')
if elem_iguais (lista2)==True:
    print('S')
else:
    print('N')

if crescente (lista3)==True:
    print('S')
else:
    print('N')
if decrescente (lista3)==True:
    print('S')
else:
    print('N')
if elem_iguais (lista3)==True:
    print('S')
else:
    print('N')