# -*- coding: utf-8 -*-

def crescente(lista):
    #escreva o códintgo da função crescente aqui
    for i in range (0,n,1):
        if lista[i]<lista[i+1]:
            return true
        else:
            return false

#escreva as demais funções
def descrescente(lista):
    for i in range(0,n,1):
        if lista[i]>lista[i+1]:
            return true
        else:
            return false
def igualdade(lista):
    for i in range(0,n,1):
        if lista[i]==lista[i+1]:
            return  true

#escreva o programa principal
a=[]
b=[]
c=[]
n=int(input('Digite a quantidade: '))
for i in range(0,n,1) :
    a.append(int(input('Digite o numero: ')))
    b.append(int(input('Digite o numero: ')))
    c.append(int(input('Digite o numero: ')))
print crescente(a)




