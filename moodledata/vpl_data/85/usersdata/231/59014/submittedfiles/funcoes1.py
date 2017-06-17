# -*- coding: utf-8 -*-

def crescente(lista):
    contd=0
    for i in range(0,len(lista)-1,1):
        if lista[i]<(lista[i+1]):
            contd=contd+1
    if (contd)==len(lista)-1:
        return True
    else:
        return False
            
    #escreva o código da função crescente aqui
def decrescente(lista):
    contc=0
    for i in  range(0,len(lista)-1,1):
        if lista[i]>(lista[i+1]):
            contc=contc+1
    if contc==len(lista)-1:
        return True
    else:
        return False
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista)-1,1):
        if lista[i]==(lista[i+1]):
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False 
a=[]
b=[]
c=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    a.append(input('lista A- %d° valor:'%i))
for i in range(0,n,1):
    b.append(input('lista B- %d° valor:'%i))
for i in range(0,n,1):
    c.append(input('lista C- %d° valor:'%i))

def teste(a):
    if crescente(a):
        print('S')
    else:
        print('N')
    if decrescente(a):
        print('S')
    else:
        print('N')
    if consecutivos(a):
        print('S')
    else:
        print('N')
teste(a)
teste(b)
teste(c)
    
#escreva as demais funções





#escreva o programa principal
