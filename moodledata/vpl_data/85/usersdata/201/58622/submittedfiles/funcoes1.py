# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos:'))
lista1=[]
lista2=[]
lista3=[]
def crescente (lista):
    #escreva o código da função crescente aqui
    
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

#escreva as demais funções

def decrescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def quantidade (lista,x):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]==x:
            cont=cont+1
    return (cont)

#escreva o programa principal

n=int(input('Digite um valor'))
a=[]
for i in range(1,n+1,1):
    num=float(input('Digite um número:'))
    a.append(num)
if crescente (a):
    print('S')
else:
    print('N')
    




























