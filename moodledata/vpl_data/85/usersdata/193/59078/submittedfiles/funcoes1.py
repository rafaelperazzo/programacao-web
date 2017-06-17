# -*- coding: utf-8 -*-

def crescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return True
    else:
        return False
        
def decrescente(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return True
    else:
        return False
        
def iguais(lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True
    return False
    
n=int(input('digite o tamanho da lista:'))
x=[]
for i in range(0,n,1):
    v1=int(input('digite os elementos:'))
    x.append(v1)

y=[]
for i in range(0,n,1):
    v2=int(input('digite os elementos:'))
    y.append(v2)
    
w=[]
for i in range(0,n,1):
    v3=int(input('digite os elementos:'))
    w.append(v3)

if crescente(x):
    print('S')
else:
    print('N')
if decrescente(x):
    print('S')
else:
    print('N')
if iguais(x):
    print('S')
else:
    print('N')  
    
    
if crescente(y):
    print('S')
else:
    print('N')
if decrescente(y):
    print('S')
else:
    print('N')
if iguais(y):
    print('S')
else:
    print('N')  
    
if crescente(w):
    print('S')
else:
    print('N')
if decrescente(w):
    print('S')
else:
    print('N')
if iguais(w):
    print('S')
else:
    print('N')    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
