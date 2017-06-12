# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos:'))
lista1=[]
lista2=[]
lista=[]
def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

#escreva as demais funções





#escreva o programa principal
