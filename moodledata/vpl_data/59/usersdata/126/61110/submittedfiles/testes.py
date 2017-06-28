# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#criando uma função para transformar o número em lista#
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
        A=LISTA(NUMERO)
        for i in range(0,len(A),1):
            soma=soma+A[i]**2
        NUMERO=soma
    if soma==1:
        return True
    else:
        return False
NUMERO=int(input('Digite um número para ser testado:'))

if FELIZ(NUMERO):
    print('SIM, ele é feliz')
else:
    print('NÃO, ele não é feliz')


