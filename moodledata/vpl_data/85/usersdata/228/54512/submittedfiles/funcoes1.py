# -*- coding: utf-8 -*-
n=int(input('digite o número de elementos:'))
lista1=[]
lista2=[]
lista3=[]
for i in range(1,n+1,1):
    elemento1=int(input('digite o elemento:'))
    lista1.append(elemento1)


    elemento2=int(input('digite o elemento:'))
    lista2.append(elemento2)


    elemento3=int(input('digite o elemento:'))
    lista3.append(elemento3)

def crescente(a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]<a[i+1]:
            cont=cont+1
            if cont==len(a)-1:
                return ('S')
            
            else:
                return ('N')
            
def decrescente(a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]>a[i+1]:
            cont=cont+1
            if cont==len(a)-1:
                return ('S')
            else:
                return ('N')    
    
def elementosiguais(a):
    cont=0
    for i in range(0,len(a)-1,1):
        if a[i]==a[i+1]:
            cont=cont+1
    if cont==0:
        return ('S')
    else:
        return ('N')
    
print(crescente(lista1))
print(decrescente(lista1))
print(elementosiguais(lista1))

print(crescente(lista2))
print(decrescente(lista2))
print(elementosiguais(lista2))

print(crescente(lista3))
print(decrescente(lista3))
print(elementosiguais(lista3))
