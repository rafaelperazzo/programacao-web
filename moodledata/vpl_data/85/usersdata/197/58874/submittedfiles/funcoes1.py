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
        
def descrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
        
def iguais (lista):
    
    for i in range(1,len(lista),1):
        if lista[i]==lista[i+1]:
            return True
        else:
            return False
            
n=int(input('Digite o numero de elementos da lista:'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    numero=int(input('Digite um elemento da lista a:')
    a.append(numero)
    
for i in range(1,n+1,1):
    numero=int(input('Digite um elemento da lista b:')
    b.append(numero)
    
for i in range(1,n+1,1):
    numero=int(input('Digite um elemento da lista c:')
    c.append(numero)
    
if crescente(a)==True:
    print('S')
else:
    print('N')
if descrescente(a)==True:
    print('S')
else:
    print('N')
if iguais(a)==True:
    print('S')
else:
    print('N')
if crescente(b)==True:
    print('S')
else:
    print('N')
if descrescente(b)==True:
    print('S')
else:
    print('N')
if iguais(b):
    print('S')
else:
    print('N')
if crescente(c)==True:
    print('S')
else:
    print('N')
if descrescente(c)==True:
    print('S')
else:
    print('N')
if iguais(c)==True:
    print('S')
else:
    print('N')