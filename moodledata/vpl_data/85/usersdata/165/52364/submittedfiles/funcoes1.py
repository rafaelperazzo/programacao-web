# -*- coding: utf-8 -*-
def crescente(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente(lista):
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
        if i==0:    
            if lista[i]==lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]==lista[i-1]:
                cont=cont+1
        else:
            if lista[i]==lista[i-1] or lista[i]==lista[i+1]:
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
    valor=float(input('digite um valor:'))
    a.append(valor)
for i in range(1,n+1,1):
    x=float(input('digite um x:'))
    b.append(x)
for i in range(1,n+1,1):
    numero=float(input('digite um numero:'))
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
            
        
    
    
    
    

