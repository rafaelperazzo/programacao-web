# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont!=len(lista)-1:
        return True
    else:
        return False
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
        if cont==0:
            return False
        else:
            return True
a=[]
b=[]
c=[]
n=int(input('Tamanho da lista:'))
for i in range(1,n+1,1):
    valora=int(input('Digite o valor a:'))
    a.append(valora)
for i in range(1,n+1,1):
    valorb=int(input('Digite o valor b:'))
    b.append(valorb)
for i in range(1,n+1,1):
    valorc=int(input('Digite o valor c:'))
    c.append(valorc)
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
if consecutivos(c):
    print('S')
else:
    print('N')
if descrescente(c):
    print('S')
else:
    print('N')
    





#escreva o programa principal
