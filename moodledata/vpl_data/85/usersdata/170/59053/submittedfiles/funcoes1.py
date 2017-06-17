# -*- coding: utf-8 -*-
def crescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False


        

    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
