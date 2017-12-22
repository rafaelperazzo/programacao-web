# -*- coding: utf-8 -*-

def crescente (lista):
    for i in range (0,len(lista),1) :
        if lista[i] > lista[i+1] :
            break
        return(True)
        
    #escreva o código da função crescente aqui


#escreva as demais funções
def decrescente (lista) :
    for i in range(0,len(lista),1) :
        if lista[i] < lista[i+1] :
            break
        return(True)
def iguais (lista) :
    cont = 0
    for i in range(0,len(lista),1) :
        if lista[i] == lista[i+1] :
            cont = cont + 1
        if cont > 0 :
            return(True)
        else :
            return(False)





#escreva o programa principal
