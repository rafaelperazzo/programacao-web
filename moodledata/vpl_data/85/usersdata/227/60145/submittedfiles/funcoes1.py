# -*- coding: utf-8 -*-

def crescente (lista):
    #escreva o código da função crescente aqui
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
    for i in range(0,len(lista)-1,1):
        if lista[i]>lista[i+1]:
            contc=contc+1
    if  contc==len(lista)-1:
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

#escreva as demais funções

n=int(input('Quantidade de lementos:'))

a=[]
b=[]
c=[]

for i in range(1,n+1,1):
    a.append(input('Lista A - %d° Valor:'%i))
for i in range(1,n+1,1):
    b.append(input('Lista B - %d° Valor:'%i))
for i in range(1,n+1,1):
    c.append(input('Lista C - %d° Valor:'%i))





#escreva o programa principal
def teste(a):
    if crescente(a):
        print('S')
    else:
        print('N')
    if decrescente(a):
        print('S')
    else:
        print('N')
    if consecutivo(a):
        print('S')
    else:
        print('N')
        
teste(a)
teste(b)
teste(c)