# -*- coding: utf-8 -*-

def crescente (lista):
    cont=0
    for i in range (1,len(lista),1):
        if lista[i]>lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def decrescente (lista):
    cont=0
    for i in range (1,len(lista),1):
        if lista[i]<lista[i-1]:
            cont=cont+1
    if cont==len(lista)-1:
        return True
    else:
        return False

def consecutivo (lista):
    cont=0
    for i in range (1,len(lista),1):
        if lista[i]==lista[i-1]:
            cont=cont+1
    if cont!=0:
        return True
    else:
        return False
        
def resposta (lista):
    if crescente(lista):
        print(''S'')
    else:
        print(''N'')
    if decrescente(lista):
        print(''S'')
    else:
        print(''N'')
    if consecutivo (lista):
        print(''S'')
    else:
        print(''N'')

#escreva o programa principal
n = int(input('n:'))
A=[]
B=[]
C=[]

for i in range (1,n+1,1):
    numero = float(input('num:'))
    A.append (numero)
for i in range (1,n+1,1):
    numero = float(input('num:'))
    B.append (numero)
for i in range (1,n+1,1):
    numero = float(input('num:'))
    C.append (numero)
    
resposta (A)
resposta (B)
resposta (C)

    

    
    

