# -*- coding: utf-8 -*-
#FUNÇÕES
def crescente(lista) :
    if len(lista)==1 :
        return(False)
    cont = 0
    for i in range(0,len(lista),1) :
        if (i==0) :
            if(lista[i]<lista[i+1]) :
                cont = cont+1
        elif (i==(len(lista)-1)) :
            if lista[len(lista)-2] < lista[len(lista)-1] :
                cont = cont+1
        else :
            if lista[i]<lista[i+1] :
                cont = cont+1
    if cont == len(lista) :
        return(True)
    else :
        return(False)
def decrescente(lista) :
    if len(lista)==1 :
        return(False)
    cont = 0
    for i in range(0,len(lista),1) :
        if (i==0) :
            if(lista[i]>lista[i+1]) :
                cont = cont+1
        elif (i==len(lista)-1) :
            if lista[len(lista-2)] > lista[len(lista)-1] :
                cont = cont+1
        else :
            if lista[i]>lista[i+1] :
                cont = cont+1
    if cont == len(lista) :
        return(True)
    else :
        return(False)
            
def pico(lista):
    maior = max(lista)
    imaior = lista.index(maior)
    an = []
    de = []
    for i in range(0,imaior+1,1):
        elemento_an = lista[i]
        an.append (elemento_an)
    for i in range ((imaior+1),len(lista),1) :
        elemento_de = lista[i]
        de.append(elemento_de)
    if crescente (an) and decrescente(de) :
        return(True)
    else :
        return(False)
    
#ENTRADA
n = int(input('Digite a quantidade de elementos da lista: '))
a = []
for i in range (0,n,1) :
    valor_a = float(input('Digite o elemento da lista a : '))
    a.append(valor_a)
if pico(a) :
    print('S')
else :
    print('N')

