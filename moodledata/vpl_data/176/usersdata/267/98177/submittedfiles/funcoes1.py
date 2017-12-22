# -*- coding: utf-8 -*-

#escreva o código da função crescente aqui
def crescente (lista):
    for i in range(0,len(lista)-1,1):
        if (lista[i]>lista[i+1]):
            return('N')
    return('S')
        
#escreva as demais funções
def decrescente (lista):
    for i in range(0,len(lista)-1,1):
        if (lista[i]<lista[i+1]):
            return('N')
    return('S')


def iguais (lista):
    for i in range(0,len(lista)-1,1):
        if (lista[i]==lista[i+1]):
            return('S')
    return('N')

#escreva o programa principal
n=int(input('Quantidade de elementos de cada lista: '))
a=[]
b=[]
c=[]

for i in range(0,n,1):
    elem_a=float(input('Forneça os elementos de "a": '))
    a.append(elem_a)
print()
for i in range(0,n,1):
    elem_b=float(input('Forneça os elementos de "b": '))
    b.append(elem_b)
print()
for i in range(0,n,1):
    elem_c=float(input('Forneça os elementos de "c": '))
    c.append(elem_c)
print()
print(crescente(a))
print(decrescente(a))
print(iguais(a))
print(crescente(b))
print(decrescente(b))
print(iguais(b))
print(crescente(c))
print(decrescente(c))
print(iguais(c))
