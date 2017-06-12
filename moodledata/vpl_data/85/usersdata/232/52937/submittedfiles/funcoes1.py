# -*- coding: utf-8 -*-
a=[ ]
b=[ ]
c=[ ]
n=int(input('Digite o número de elemento das listas: '))

for i in range (1,n+1,1):
    num1=int(input('Digite um elemento da lista a: '))
    a.append(num1)

for i in range (1,n+1,1):
    num2=int(input('Digite um elemento da lista b: '))
    b.append(num2)
    
for i in range (1,n+1,1):
    num3=int(input('Digite um elemento da lista c: '))
    c.append(num3)
    
def crescente (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i+1]>lista[i]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
    #escreva o código da função crescente aqui

#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def consecutivo (lista):
    cont=0
    for i in range (0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont==0:
        return False
    else:
        return True
#escreva o programa principal
print(crescente(a))
print(decrescente(a))
print(consecutivo(a))
print(crescente(b))
print(decrescente(b))
print(consecutivo(b))
print(crescente(c))
print(decrescente(c))
print(consecutivo(c))