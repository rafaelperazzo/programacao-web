# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    contador=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i-1]:
            contador=contador+1
    if contador==0:
        return True
    else:
        return False
        
        
def decrescente (lista):
    condador=0
    for i in range(1,len(lista),1):
        if lista[i]<lista[i+1]:  
            contador=contador+1
        if contador==len(lista)-1:
            return True
        else:
            return False
            
            
def consecutivo (lista):
    for i in range(1,len(lista),1):
        if lista[i]==lista[i+1]:
            return True
        else:
            return False
    
n=int(input('digite o tamanho da lista:'))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    x=int(input('digite um numero da L1:'))
    a.append(x)
    
for i in range(0,n,1):
    y=int(input('digite um numero da L2:'))
    b.append(y)

for i in range(0,n,1):
    z=int(input('digite um numero da L3:'))
    c.append(z)

#escreva o programa principal



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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    