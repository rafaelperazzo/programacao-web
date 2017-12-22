# -*- coding: utf-8 -*-

def crescente(lista):
    contc=0
    cont1=0
    cont2=0
    cont3=0
    for i in range(0,len(lista),1):
        if i==0:
            cont1=cont1+1
        elif i==len(lista) and lista[i]>lista[i-1]:
            cont2=cont2+1
        if lista[i]>lista[i-1]:
            cont3=cont3+1
    conct=cont1+cont2+cont3
    return(contc)
    
def decrescente(lista):
    n=int(input('digite a quantidade de termos da lista: '))
    contd=0
    cont1=0
    cont2=0
    cont3=0
    for i in range(0,len(lista),1):
        if i==0:
            cont1=cont1+1
        elif i==len(lista) and lista[i]<lista[i-1]:
            cont2=cont2+1
        if lista[i]<lista[i-1]:
            cont3=cont3+1
    contd=cont1+cont2+cont3
    return(contd)

n=int(input('digite a quantidade de termos da listas: '))
a=[]
b=[]
c=[]
for i in range(0,n,1):
    valor=float(input('digite os valores da lista A: '))
    a.append(valor)
for i in range(0,n,1):
    valor=float(input('digite os valores da lista B: '))
    b.append(valor)
for i in range(0,n,1):
    valor=float(input('digite os valores da lista C: '))
    c.append(valor)
A=lista(a)
B=lista(b)
C=lista(c0
if (A!=0):
    if contc==n:
        print('S')
        print('N')
        print('N')
    elif contd==n:
        print('N')
        print('S')
        print('N')
    else:
        print('N')
        print('N')
        print('S')
if (B!=0):
    if contc==n:
        print('S')
        print('N')
        print('N')
    elif contd==n:
        print('N')
        print('S')
        print('N')
    else:
        print('N')
        print('N')
        print('S')
if C!=0:
    if contc==n:
        print('S')
        print('N')
        print('N')
    elif contd==n:
        print('N')
        print('S')
        print('N')
    else:
        print('N')
        print('N')
        print('S')