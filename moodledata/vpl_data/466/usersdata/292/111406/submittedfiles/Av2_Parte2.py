# -*- coding: utf-8 -*-
######################################### -> FUNÇÃO
def crescente(lista):
    crescente, decrescente, iguais = ("S","N","N"), ("N","S","N"), ("N","N","S)
    cont_cres, cont_decres, cont_igual = 0, 0, 0
    
    for i in range(1, len(lista)):
        cont_cres, cont_decres = 0, 0
        
        if lista[i-1] < lista[i]:
            cont_cres += 1
            
        elif lista[i-1] > lista[i]:
            cont_decres += 1
            
        else:
            cont_igual += 1
            break
    
    if cont_igual == 1:
        return iguais
        
    elif cont_cres != 0:
        return crescente
        
    else:
        return decrescente
        
######################################### - > PROGRAMA PRINCIPAL    
n = int(input())