# -*- coding: utf-8 -*-
def contido(lista1,lista2):
    cont_contido=0
    
    for i in range(0,len(lista2),1):
        if lista2[i] in lista1:
            cont_contido= cont_contido + 1 
        return(cont_contido)
listaA=[]
listaB=[]
n1=int(input("Digite o numero de elementos da 1ª lista :"))
n2=int(input("Digite o numero de elementos da 2ª lista :"))        

for i in range(0,n1,1):
    listaA.append(int(input("Digite o valor do %dº valor da 1ª lista: "%(i+1))))
for i in range(0,n2,1):
    listaB.append(int(input("Digite o valor do %dº valor da 2ª lista: "%(i+1))))
    
print(contido(listaA,listaB))