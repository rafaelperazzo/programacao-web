# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO


#Criando uma função para transformar o número em lista#
def LISTA(NUMERO):
    LISTA = []
    while NUMERO>0:
        RESTO = NUMERO%10 #caminhando pelos termos do número#
        LISTA.append(RESTO) #adicionando cada termo do número em uma lista#
        NUMERO = NUMERO//10 #atualizando o número, retirando o seu último dígito#
    return LISTA
    
#função para determinar se o número é feliz#
def FELIZ(NUMERO):
    while NUMERO>1:
        soma = 0
        A = LISTA(NUMERO) #chamando a função 'LISTA', e a transformando#
        for i in range(0,len(A),1):
            soma = soma + A[i]**2 #soamndo os termos da lista#
        NUMERO=soma #atualizando o número#
    if soma == 1:
        return True
    else:
        return False
NUMERO = int(input('Digite um número para ser testado:'))

if FELIZ(NUMERO):
    print('SIM, ele é feliz')
else:
    print('NÃO, ele não é feliz')


