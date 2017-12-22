# -*- coding: utf-8 -*-
def contido (lista_1,lista_2):
    cont_contido=0
    listaX = []
    listaY = []
    t1 = len(lista_1)
    t2 = len(lista_2)
    if t1 < t2:
        listaX = lista_1
        listaY = lista_2
    else:
        listaX = lista_2
        listaY = lista_1
    for i in range (0,len(lista_X),1):
        if lista_X[i] in lista_Y:
            cont_contido+=1
    return (cont_contido)
lista_A=[]
lista_B=[]
lista_1=int(input("digite a quantidade de elementos da lista_1:"))
lista_2=int(input("digite a quantidade de elementos da lista_2:"))
for i in range (0,lista_1,1):
    lista_A.append (int(input(" digite o %dº elemento da lista_A: "%(i+1))))
for i in range (0,lista_2,1):    
    lista_B.append (int(input(" digite o %dº elemento da lista_B: "%(i+1))))
print (contido(lista_A,lista_B))    