# -*- coding: utf-8 -*-

def pico(n,lista):
    cont_crescente=0
    cont_decrescente=0
    for i in range(0,n-1,1):
        if lista[i]<lista[i+1]:
            cont_crescente= cont_crescente + 1
        else:
            break
    for i in range(cont_crescente,n-1,1):
        if lista[i]>lista[i+1]:
            cont_decrescente= cont_decrescente + 1
        else:
            break
        
            if cont_crescente + cont_decrescente == len(lista)-1 and cont_crescente>0 and cont_decrescente<0:
        return("S")
    else:
        return("N")
print(pico(3,[1,5,3]))

