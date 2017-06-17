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
n1=int(input('Digite o tamanho da lista 1:'))
n2=int(input('Digite o tamanho da lista 2:'))
n3=int(input('Digite o tamanho da lista 3:'))
a=[]
b=[]
c=[]
for i in range(1,n1+1,1):
    a.append(int(input('Digite o valor para lista 1:')))
for i in range(1,n2+1,1):
    b.append(int(input('Digite o valor para lista 2:')))
for i in range(1,n3+1,1):
    c.append(int(input('Digite o valor para lista 3:')))
if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if consecutios(a):
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
if consecutios(b):
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
if consecutios(c):
    print('S')
else:
    print('N')