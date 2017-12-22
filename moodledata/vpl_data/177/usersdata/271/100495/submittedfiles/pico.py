# -*- coding: utf-8 -*-
#FUNÇÕES
def pico(lista):
    maior = max(lista)
    imaior = lista.index(maior)
    an = []
    de = []
    for i in range(0,imaior+1,1):
        elemento_an = lista[i]
        an.append (elemento_an)
    for i in range (maior+1,len(lista),1) :
        elemento_de = lista[i]
        de.append(elemento_de)
    if crescente (an) and decrescente(de) :
        return(True)
    else :
        return(False)
    
    
    
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
