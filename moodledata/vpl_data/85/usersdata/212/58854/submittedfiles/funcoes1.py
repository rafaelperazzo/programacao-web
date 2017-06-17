# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    i=1
    while 1<len(lista)-2:
        if lista[i]<lista[i-1]:
            return(1)
        i=i+1
    return(2)
#escreva as demais funções
def decrescente (lista):
    i=1
    while 1<len(lista)-1:
        if lista[i]>lista[i-1]:
            return(1)
        i=i+1
    return(2)
def consecutivo(lista):
    i=1
    while 1<len(lista)-1:
        if lista[i]==lista[i-1]:
            return(1)
        i=i+1
    return(2)
#escreva o programa principal
n=int(input('digite o tamanho das listas:'))
a=[]
b=[]
c=[]
i=0
while i<n:
    num=int(input('digite um número para ista A:'))
    a.append(num)
    i=i+1
i=0
while i<n:
    num=int(input('digite um número para ista B:'))
    b.append(num)
    i=i+1
i=0
while i<n:
    num=int(input('digite um número para ista C:'))
    c.append(num)
    i=i+1
if crescente(a)==2:
    print('s')
else:
    print('N')
if decrescente(a)==2:
    print('s')
else:
    print('N')
if consecutivo(a)==1:
    print('s')
else:
    print('N')
if crescente(b)==2:
    print('s')
else:
    print('N')
if decrescente(b)==2:
    print('s')
else:
    print('N')
if consecutivo(b)==1:
    print('s')
else:
    print('N')
if crescente(c)==2:
    print('s')
else:
    print('N')
if decrescente(c)==2:
    print('s')
else:
    print('N')
if consecutivo(c)==1:
    print('s')
else:
    print('N')