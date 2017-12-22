# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    for i in range(0,n,1):
        if ((lista[i])<(lista[(i+1)])):
            return True
        else:
            return False
    

#escreva as demais funções
def consec(lista):
    for i in range(0,n,1):
        if ((lista[i])==(lista[(i+1)])):
            return True
        else:
            return False

def decrescente(lista):
    for i in range(0,n,1):
        if ((lista[i])>(lista[(i+1)])):
            return True
        else:
            return False


#escreva o programa principal
n=float(input('Digite o tamanho da lista: '))
lista_0=[]
lista_1=[]
lista_2=[]
for a in range(0,3,1):
    for lista in range(0,n,1):
        num=float(input('Digite o numero da lista: '))
        lista_(a).append(num)
        