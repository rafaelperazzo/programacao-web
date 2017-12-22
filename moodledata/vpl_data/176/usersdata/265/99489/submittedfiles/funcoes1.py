# -*- coding: utf-8 -*-

def crescente(lista):
    cont=0
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
    cont=cont1+cont2+cont3
    if cont==n:
        return(True)
    else:
        return(False)
    
def decrescente(lista):
    cont=0
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
    cont=cont1+cont2+cont3
    if cont==n:
        return(True)
    else:
        return(False)
        
n=int(input('digite a quantidade de termos da listas: '))
a=[]
b=[]
c=[]
for i range(0,n,1):
    valor=float(input('digite os valores da lista: '))
    a.append(valor)
for i range(0,n,1):
    valor=float(input('digite os valores da lista: '))
    b.append(valor)
for i range(0,n,1):
    valor=float(input('digite os valores da lista: '))
    c.append(valor)
