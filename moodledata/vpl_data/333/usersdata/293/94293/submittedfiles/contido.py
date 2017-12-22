# -*- coding: utf-8 -*-
def contido(lista1,lista2):
    cont_contido=0
    
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            cont_contido= cont_contido + 1
    return(cont_contido)
listaA=[22,11,10,8,12,76,50]
listaB=[5,9,76,20,21]

print(contido(listaA,listaB))
    
    
