# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos:')):
a=[]
b=[]
c=[]

def crescente (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            return True
    return False

#escreva as demais funções
def decrescente(lista):
    for i in range(0,(lista)-1,1):
        if lista[i]>lista[i+1]:
            return True
    return False
    
def numiguais(lista):
    for i in range(0,(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
    return False



for i in range(0,n,1):
    x=float(input('Digite os elementos:')):
    a.append(x)
for i in range(0,n,1):
    y=float(input('Digite os elementos:')):
    b.append(y)
for i in range(0,n,1):
    w=float(input('Digite os elementos:')):
    c.append(w)
    
if crescente (a):
    print('S')
else:
    print('N')
    
if decrescente (a):
    print('S')
else:
    print('N')
    
if numiguais (a):
    print('S')
else:
    print('N')
    
if crescente (b):
    print('S')
else:
    print('N')
    
if decrescente (b):
    print('S')
else:
    print('N')
    
if numiguais (b):
    print('S')
else:
    print('N')
    
    
if crescente (c):
    print('S')
else:
    print('N')
    
if decrescente (c):
    print('S')
else:
    print('N')
    
if numiguais (c):
    print('S')
else:
    print('N')