# -*- coding: utf-8 -*-

def crescente (lista):
    contd=0
    for i in range(0,len(lista),-1,1):
        if lista[i]<lista[i+1]:
            contd=contd+1
    if (contd)==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    contc=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contc=contc+1
    if contc==len(lista)-1:
        return True
    else:
        return False
def consecutivos (lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False
A= int(input('Quantidade de elementos' ))
c=[]
d=[]
e=[]
for i in range(1,A+1,1):
    c.append(input('Lista C - %d° Valor: '%i))
for i in range(1,A+1,1):
    d.append(input('Lista D - %d° Valor: '%i))
for i in range(1,A+1,1):
    e.append(input('Lista E - %d° Valor: '%i))
def teste(c):
    if crescente(c):
        print ('S')
    else:
        print ('N')
    if decrescente(c):
        print ('S')
    else:
        print ('N')
    if consecutivos(c):
        print ('S')
    else:
        print ('N')
teste(c)
teste(d)
teste(e)
    


    
    









