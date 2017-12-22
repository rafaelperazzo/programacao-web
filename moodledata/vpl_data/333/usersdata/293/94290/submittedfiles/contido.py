# -*- coding: utf-8 -*-
def contido(lista1,lista2):
    cont_contido=0
    
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            cont_contido= cont_contido + 1
    return(cont_contido)
listaA=[1,2,3,4,5,6,7,8,9,10]
listaB=[
    
    
