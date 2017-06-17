# -*- coding: utf-8 -*-
def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i+1]:
            cont=cont+1
    if cont==(len(lista)-1):
        return S
    else:
        return N
#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i+1]:
        
        else:
            cont=1
    if cont==0:
        return S
    else:
        return N

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
cr=crescente(a)
print(cr)
d=decrescente(a)
print(d)
i=iguais(a)
print(i)
cr=crescente(b)
print(cr)
d=decrescente(b)
print(d)
i=iguais(b)
print(i)
cr=crescente(c)
print(cr)
d=decrescente(c)
print(d)
i=iguais(c)
print(i)