# -*- coding: utf-8 -*-

def crescente (lista):
    cont_crescente=0
    for i in range(0,n-1,1):
        if lista_crescente[i]<lista_crescente[i+1]:
            cont_crescente= cont_crescente + 1
    if cont_crescente==len(lista_crescente)-1:
        return ("S")
    else:
        return ("N")
        
def decrescente(n,lista_decrescente):
    cont_consecutivo=0
    for i in range(0,n-1,1):
        if lista_consecutiva[i]==lista_consecutiva[i+1]:
            cont_decrescente= cont_decrescente + 1
    if cont_decrescente==len(lista_decrescente)-1:
        return ("S")
    else:
        return ("N")
        
def consecutivo(n,lista_consecutiva):
    cont_consecutivo=0
    for i in range(0,n-1,1):
        if lista_consecutiva[i]==lista_consecutiva[i+1]:
            cont_consecutivo= cont_consecutivo + 1
    if cont_consecutivo>0:
        return ("S")
    else:
        return ("N")
print(crescente(6,[1,2,3,4,5,6]))
print(decrescente(6,[1,2,3,4,5,6]))
print(consecutivo(6,[1,2,3,4,5,6]))
print(crescente(6,[7,6,5,4,3,2]))
print(decrescente(6,[7,6,5,4,3,2]))
print(consecutivo(6,[7,6,5,4,3,2]))
print(crescente(6,[9,8,8,8,9,1]))
print(decrescente(6,[9,8,8,8,9,1]))
print(consecutivo(6,[9,8,8,8,9,1]))
    







#escreva o programa principal
