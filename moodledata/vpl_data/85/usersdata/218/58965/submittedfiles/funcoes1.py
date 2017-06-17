# -*- coding: utf-8 -*-
def crescente (lista):
    #escreva o código da função crescente aqui
    cont=1
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1]:
                cont=cont+1
    if cont==len(lista):
        return True
    else:
        return False
#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    return cont

def iguais (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
            cont=1
        
    if cont==1:
        return S
    else:
        return N  
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
if crescente(a):
    print('S')
else:
    print('N')
if decrescente(a)==(len(lista)-1):
    print ('S')
else:
    print('N')
valor=iguais(a)
print(valor)


if crescente(b):
    print('S')
else:
    print('N')
    
if crescente(c):
    print('S')
else:
    print('N')    