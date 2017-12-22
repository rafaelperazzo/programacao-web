# -*- coding: utf-8 -*-

def pico(n,lista):
    cont_crescente=0
    cont_decrescente=0
    for i in range(0,n-1,1):
        if lista[i]<lista[i+1]:
            cont_crescente= cont_crescente + 1
        elif lista[i]>lista[i+1]:
            cont_decrescente= cont_decrescente + 1
    
    if cont_crescente + cont_decrescente == len(lista)-1:
        return("S")
    else:
        return("N")
print(pico(3,[1,2,1]))

