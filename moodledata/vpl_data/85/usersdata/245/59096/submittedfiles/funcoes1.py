# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def consecutivos (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
    return False
n=int(input('Digite o tamanho das listas :'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    a.append(int(input('Digite o valor para lista 1:')))
for i in range(1,n+1,1):
    b.append(int(input('Digite o valor para lista 2:')))
for i in range(1,n+1,1):
    c.append(int(input('Digite o valor para lista 3:')))
def teste (a):
    if crescente(a):
        print('S')
    else:
        print('N')
    if decrescente(a):
        print('S')
    else:
        print('N')
    if consecutivos(a):
        print('S')
teste(a)
teste(b)
teste(c)