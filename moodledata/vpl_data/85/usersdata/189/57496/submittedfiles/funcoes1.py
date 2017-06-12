# -*- coding: utf-8 -*-
a=[]
b=[]
c=[]
def crescente (lista):
    cont=0
    for i in range(1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
        
def decrescente (lista):
    cont=0
    for i in range (1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont-cont+1
    if cont==len(lista):
        return True
    else:
        return False

def conseutivos (lista):
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            return True

        


#escreva as demais funções





#escreva o programa principal
