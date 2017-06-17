# -*- coding: utf-8 -*-

def crescente (lista):
    #código da função crescente aqui
    contd=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<lista[i+1]:
            contd=contd+1
    if (contd)==len(lista)-1:
        return True
    else:
        return False
def decrescente (lista):
    contc=0
    for i in range (0,len(lista)-1,1):
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
H = int(input('quantidade de elementos:'))
d=[]
e=[]
f=[]
for i in range(1,H+1,1):
    d.append(input('Lista D - %d° Valor: '%i))
for i in range(1,H+1,1):
    e.append(input('Lista E - %d° Valor: '%i))
for i in range(1,H+1,1):
    f.append(input('Lista F - %d° Valor: '%i))
def teste(d):
    if crescente(d):
        print ('S')
    else: 
        print ('N')
    if decrescente(d):
        print ('S')
    else:
        print('N')
    if consecutivos(d):
        print ('S')
    else:
        print ('N')
teste(d)
teste(e)
teste(f)


        
    







