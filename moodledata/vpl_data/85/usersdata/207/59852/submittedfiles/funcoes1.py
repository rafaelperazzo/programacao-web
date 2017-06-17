# -*- coding: utf-8 -*-

def crescente (lista):
    #código da função crescente
    contd=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            contd=contd+1
    if (contd)==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    #código da função decrescente
    contc=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contc=contc+1
    if contc==len(lista)-1:
        return True
    else:
        return False
def consecutivos (lista):
    #código da função de elementos consecutivos
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False

#escreva as demais funções
# pedir a quantidade de elementos das listas
n=int(input('Quantidade de elementos:'))
# criar as listas vazias
v=[]
l=[]
s=[]
# inserir elementos à lista
for i in range(1,n+1,1):
    v.append(input('Lista V - %d° valor: '%i))
for i in range(1,n+1,1):
    l.append(input('Lista L - %d° valor: '%i))
for i in range(1,n+1,1):
    s.append(input('Lista S - %d° valor: '%i))


 
def teste(a):
    if crescente(a):
        print ('S')
    else:
        print ('N')
    if decrescente(a):
        print ('S')
    else:
        print ('N')
    if consecutivos(a):
        print ('S')
    else:
        print ('N')
        
# chamando a função teste
teste(a)
teste(b)
teste(c)



