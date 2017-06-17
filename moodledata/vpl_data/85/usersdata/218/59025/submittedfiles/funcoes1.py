# -*- coding: utf-8 -*-
def crescente (lista):
    cont=1
    for i in range(1,len(lista),1):
        if lista[1]>lista[i-1]:
            cont=cont+1
    if cont==len(lista):
        return True
    else:
        return False

def decrescente (lista):
    cont=1
    for i in range(1,len(lista),1):
        if lista[1]<lista[i-1]:
            cont=cont+1
    if cont==len(lista):
        return True
    else:
        return False
def iguais (lista):
    for i in range(1,len(lista),1):
        if i<len(lista)-1:
            if lista[i]==lista[i+1]:
                return True
    return False
        
    
#escreva as demais funções

#escreva o programa principal
n=int(input('digite o numero de elementos das listas:'))
a=[]
b=[]
c=[]
for i in range (0,n,1):
    valor=int(input('digite o elemento a ser anexado a lista a:'))
    a.append(valor)
for i in range (0,n,1):
    valor=int(input('digite o elemento a ser anexado a lista b:'))
    b.append(valor)   
for i in range (0,n,1):
    valor=int(input('digite o elemento a ser anexado a lista c:'))
    c.append(valor) 
if crescente(a)==True:
    print('S')
else:
    print('N')    

if decrescente(a)==True:
    print('S')
else:
    print('N')
    
if iguais(a)==True:
    print('S')
else:
    print('N') 
  