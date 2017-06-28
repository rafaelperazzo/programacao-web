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
    #codigo da função decrescente
    contc=0
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contc=contc+1
    if contc==len(lista)-1:
        return True
    else:
        return False
def consecutivos (lista):
    #codigo da função de elementos consecutivos
    cont=0
    for i in range (0, len(lista)-1,1):
        if lista[i]==lista[i+1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False        
        
n=int(input('quantidade de elementos:'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    a.append(input('listaA - %d valor: '%i))
for i in range(1,n+1,1):
    b.append(input('listaB - %d valor: '%i))
for i in range(1,n+1,1):
    c.append(input('listaC - %d valor: '%i))
def test(a):
    if crescente(a):
        print('S')
    else:
        print ('N')
    if decrescente(a):
        print('S')
    else:
        print ('N') 
    if consecutivos(a):
        print('S')
    else:
        print ('N') 
