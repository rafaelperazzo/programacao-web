# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
    contd=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            contd=contd+1
    if (contd)==len(lista)-1:
        return true
    else:
        return false
def decrescente (lista):
    #código da função decrescente
    contc=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contc=contc+1
    if contc==len(lista)-1:
        return true
    else:
        return false
def consecutivos (lista):
    #código da função de elementos consecutivos
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
        if cont!=0:
            return true
        else:
            return false

#escreva as demais funções
#pedir a quantidade de elementos das listas
n=int(input('quantidade de elementos:'))
#criar as listas vazias
a=[]
b=[]
c=[]
#inserir elementos à lista
for i in range(1,n+1,1):
    a.append(input('lista a - %d° valor: %i))
for i in range(1,n+1,1):
    b.append(input('lista b - %d° valor: %i))
for i in range(1,n+1,1):
    c.append(input('lista c - %d° valor: %i))



def teste(a):
    if crescente(a):
        print ('s')
    else:
        print ('n')
    if decrescente(a):
        print ('n')
    else:
        print ('n')
    if consecutivo(a):
        print ('s')
    else:
        print ('n')
        
#chamando a função teste
teste(a)
teste(b)
teste(c)



#escreva o programa principal
