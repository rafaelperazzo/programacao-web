# -*- coding: utf-8 -*-
def contido(lista1, lista2):
    cont_contido=0
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            cont_contido+=1
    return(cont_contido)
listaA=[]
listaB=[]
n1=int(input('digite o numero de elementosda primeira lista: '))
n2=int(input('digite o numero de elementosda segunda lista: '))
for i in range(0,n1,1):
    listaA.append(int(input(digite o valor %d da primeira lista: '%(i+1))))
for i in range(0,n1,1):
    listaA.append(int(input(digite o valor %d da primeira lista: '%(i+1))))
    print(contido(listaA,listaB))
    


