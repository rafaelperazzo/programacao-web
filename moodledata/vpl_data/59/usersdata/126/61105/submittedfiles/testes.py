# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def LISTA(NUMERO):
    LISTA=[]
    while NUMERO>0:
        RESTO=NUMERO%10
        LISTA.append(RESTO)
        NUMERO=NUMERO//10
    return LISTA
def FELIZ(NUMERO):
    while NUMERO>1:
        soma=0
        LISTA=LISTA(NUMERO)
        for i in range(0,len(LISTA),1):
            soma=soma+LISTA[i]**2
        NUMERO=soma
    if soma==1:
        return True
    else:
        return False
NUMERO=int(input('digite um numero:'))

if FELIZ(NUMERO):
    print('s')


