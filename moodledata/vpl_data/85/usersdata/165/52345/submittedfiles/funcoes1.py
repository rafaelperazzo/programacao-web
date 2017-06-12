# -*- coding: utf-8 -*-
def crescente(lista):
    for i in range(0,len(lista),1):
        if lista[i+1]<lista[i]:
            return False
    return True        

def decrescente(lista):
    for i in range(0,len(lista),1):
        if lista[i]<lista[i+1]:
            return False
    return True

def consecutivos(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

n=int(input('digite n:'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    valor=int(input('digite um valor:'))
    a.append(valor)
for i in range(1,n+1,1):
    x=int(input('digite um x:'))
    b.append(x)
for i in range(1,n+1,1):
    numero=int(input('digite um numero:'))
    c.append(numero)
    
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
if decrescente(c):
    print('S')
else:
    print('N')
if consecutivos(c):
    print('S')
else:
    print('N')
            
        
    
    
    
    

