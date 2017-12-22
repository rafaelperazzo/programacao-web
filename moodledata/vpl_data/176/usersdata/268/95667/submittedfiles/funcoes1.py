# -*- coding: utf-8 -*-

def crescente (a):
    #escreva o código da função crescente aqui
    cont=0
    for i in range(1,len(a),1):
        if a[i] > a[i-1]:
            cont=cont+1
        else:
            break
        if cont==len(a)-1:
            return(True)
        else:
            return(False)
            


#escreva as demais funções





#escreva o programa principal
