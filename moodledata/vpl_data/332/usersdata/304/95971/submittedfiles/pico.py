# -*- coding: utf-8 -*-

def pico(lista):
    #CONTINUE...
    conta = 0
    contb = 0
    contc = 0
    for i in range(1,len(a),1):
        if(a[i]>a[i-1]) and contb==0:
            conta=conta+1
        elif(a[i]<a[i-1]):
            contb=contb+1
        else:
            contc=contc+1
            break
    if conta + contb == len(a)-1:
        return(True)
    else:
        return(False)
n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
