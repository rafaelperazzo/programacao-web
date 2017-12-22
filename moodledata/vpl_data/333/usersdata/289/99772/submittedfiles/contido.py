# -*- coding: utf-8 -*-
a=int(input("Digite a quantidade de de elementos de a: "))
b=int(input("Digite a quantidade de de elementos de b: "))
lista1=[]
lista2=[]
for i in range(0,a,1):
    lista1.append(int(input("Digite número%.d da lista1:" %(i+1))))
for i in range(0,b,1):
    lista1.append(int(input("Digite número%.d da lista2:" %(i+1))))
    
#INTERSEÇÃO DE ELEMETOS
def comuns(lista):
    comuns=[]
    for i in lista1:
        if (i in list1 and list2):
            comuns.append(i)
    return comuns
    