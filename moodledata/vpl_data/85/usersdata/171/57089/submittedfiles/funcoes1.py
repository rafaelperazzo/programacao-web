# -*- coding: utf-8 -*-
n=int(input('digite a quantidade elementos da lista:'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    valor1=int(input('digite a quantidade elementos da lista:'))
    a.append(valor1)
for i in range(1,n+1,1):
    valor2=int(input('digite a quantidade elementos da lista:'))
    b.append(valor2)
for i in range(1,n+1,1):
    c.append(valor3)
def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont==0:
        return True
    else:
        return False
#escreva o programa principal
if crescente(a):
    print('S)
else:
    print('N')
if decrescente(a):
    print('S')
else:
    print('N')
if consecutivos(a):
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
if consecutivos(b):
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
if consecutivos(c):
    print('S')
else:
    print('N')
