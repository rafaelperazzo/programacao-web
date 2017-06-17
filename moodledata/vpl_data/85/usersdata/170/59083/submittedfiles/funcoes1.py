# -*- coding: utf-8 -*-
def crescente (lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente(lista):
    cont=0
    for i in range(0,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False
        
def consecutivos(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]==lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]==lista[i-1]:
                cont=cont+1
        else:
            if lista[i]==lista[i-1] or lista[i]==lista[i+1]:
                cont=cont+1
    if cont!=0:
        return True
    else:
        return False

n=int(input('Digite n:'))
a=[]
b=[]
c=[]
for i in range(1,n+1,1):
    valor=float(input('Digite um valor:'))
    a.append(valor)
for i in range(1,n+1,1):
    x=float(input
        

    #escreva o código da função crescente aqui


#escreva as demais funções





#escreva o programa principal
