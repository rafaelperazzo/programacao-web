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
n=int(input('Digite o tamanho da lista: '))
lista1=[]
lista2=[]
lista3=[]
for a in range(0,3,1):
    for lista in range(0,n,1):
        num=int(input('Digite o numero da lista: '))
        lista.append(num)
        