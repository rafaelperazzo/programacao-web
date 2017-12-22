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

lista0=[]
for lista in range(0,n,1):
    num=float(input('Digite o numero da lista: '))
    lista0.append(num)
lista1=[]
for lista in range(0,n,1):
    num=float(input('Digite o numero da lista: '))
    lista1.append(num)
lista2=[]
for lista in range(0,n,1):
    num=float(input('Digite o numero da lista: '))
    lista2.append(num)
    
print(lista0)
print(lista1)
print(lista2)
        