# -*- coding: utf-8 -*-

def crescente (n,lista_crescente):
    #escreva o código da função crescente aqui
    cont_crescente=0
    for i in range (0,n-1,1):
        if lista_crescente[i]<(lista_crescente[i+1]):
            cont_crescente+=1
    if cont_crescente==len(lista_crescente)-1:
        return ('S')
    else:
        return ('N')
        
def decrescente (n,lista_decrescente):
    cont_decrescente=0
    for i in range (0,n-1,1):
        if lista_decrescente[i]<(lista_decrescente[i+1]):
            cont_decrescente+=1
    if cont_decrescente==len(lista_decrescente)-1:
        return ('S')
    else:
        return ('N')

def consecutivo (n,lista_consecutivo):
    #escreva o código da função crescente aqui
    cont_consecutivo=0
    for i in range (0,n-1,1):
        if lista_consecutivo[i]<(lista_consecutivo[i+1]):
            cont_consecutivo+=1
    if cont_consecutivo==len(lista_consecutivo)-1:
        return ('S')
    else:
        return ('N')
        
        
#escreva o programa principal
print (crescente(3,[1,2,3]))
print (decrescente(3,[1,2,3]))
print (consecutivo(3,[1,2,3]))
print (crescente(3,[3,2,1]))
print (decrescente(3,[3,2,1]))
print (consecutivo(3,[3,2,1]))
print (crescente(3,[1,1,2]))
print (decrescente(3,[1,1,2]))
print (consecutivo(3,[1,1,2]))