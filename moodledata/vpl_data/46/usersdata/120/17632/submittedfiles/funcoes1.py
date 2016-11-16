# -*- coding: utf-8 -*-
from  __future__  import division

def crescente(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]<lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]>lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]>lista[i-1]  and lista[i]<lista[i+1]:
                cont=cont+1
    if cont==(len(lista)):
        return True
    else:
        return False
#escreva o código da função crescente aqui
def decrescente(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]>lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]<lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]<lista[i-1] and lista[i]>lista[i+1]:
                cont=cont+1
    if cont==(len(lista)):
        return True
    else:
        return False
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[0]==lista[1]:
                cont=cont+1
        elif i==(len(lista)-1):
            if lista[len(lista)-1]==lista[len(lista)-2]:
                cont=cont+1
        else:
            if lista[i]==lista[i+1]:
                cont=cont+1
    if cont>0:
        return True
    else:
        return False
        
#escreva o programa principal
n=input('digite n:')
a=[]
b=[]
c=[]
for i in range(0,n,1):
    a.append(input('digite os elementos de a:'))
for i in range(0,n,1):
    b.append(input('digite os elementos de b:'))
for i in range(0,n,1):
    c.append(input('digite os elementos de c:'))
#saida    
#crescente
if crescente(a):
    print('S')
else:
    print('N')
if crescente(b):
    print('S')
else:
    print('N')
if crescente(c):
    print('S')
else:
    print('N')
#decrescente
if decrescente(a):
    print('S')
else:
    print('n')
if decrescente(b):
    print('S')
else:
    print('N')
if decrescente(c):
    print('S')
else:
    print('N')
#consecutivos
if consecutivos(a):
    print('S')
else:
    print('N')
if consecutivos(b):
    print('S')
else:
    print('N')
if consecutivos9c):
    print('S')
else:
    print('N')
    