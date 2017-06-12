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

def consecutivo (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]==lista[i+1]:
        if cont==0:
            return True
        else:
            return False

n=int(input('digite n:'))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    numero=int(input('digite a:'))
    a.append(numero)
    
for i in range(0,n,1):
    numero=int(input('digite b:'))
    b.append(numero)
    
for i in range(0,n,1):
    numero=int(input('digite c:'))
    c.append(numero)
    
if crescente(a)==True:
    print('S')
else:
    print('N')
if decrescente(a)==True:
    print('S')
else:
    print('N')
if consecutivo(a)==True:
    print('S')
else:
    print('N')    
    
    
if crescente(b)==True:
    print('S')
else:
    print('N')
if decrescente(b)==True:
    print('S')
else:
    print('N') 
if consecutivo(b)==True:
    print('S')
else:
    print('N') 
    
if crescente(c)==True:
    print('S')
else:
    print('N')
if decrescente(c)==True:
    print('S')
else:
    print('N')
if consecutivo(c)==True:
    print('S')
else:
    print('N') 

