# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO


#Criando uma função para transformar o número em lista#
def LISTA(NUMERO):
    LISTA=[]
    RESTO=NUMERO%10 #caminhando pelos termos do número#
    LISTA.append(RESTO) #adicionando cada termo do número em uma lista#
    return LISTA
    
#função para determinar se o número é feliz#
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


