# -*- coding: utf-8 -*-

def crescente (lista):
    cont = 0
    for i in range (0,len(lista),1) :
        if (i==0):
            if (lista[0]<lista[1]) :
                cont = cont + 1
        elif (i==len(lista)-1):
            if (lista[len(lista)-2]<lista[len(lista)-1]) :
                cont = cont + 1
        else :
            if (lista[i-1]< lista[i] < lista[i+1]) :
                cont = cont+1
    if cont == len(lista) :
        return(True)
    else :
        return(False)
        
    
        
    #escreva o código da função crescente aqui


#escreva as demais funções
def decrescente (lista) :
    cont = 0
    for i in range (0,len(lista),1) :
        if (i==0):
            if (lista[0]>lista[1]) :
                cont = cont + 1
        elif (i==len(lista)-1):
            if (lista[len(lista)-2]>lista[len(lista)-1]) :
                cont = cont + 1
        else :
            if (lista[i-1]> lista[i] > lista[i+1]) :
                cont = cont+1
    if cont == len(lista) :
        return(True)
    else :
        return(False)
def iguais (lista) :
    cont = 0
    for i in range(0,len(lista),1) :
        if (i==0) :
            if (lista[i]==lista[i+1]) :
                cont = cont+1
        elif (i==(len(lista)-1)) :
            if (lista[i-1]==lista[i]):
                cont = cont+1
        else :
            if (lista[i]==lista[i+1]) or (lista[i-1] == lista[i]) :
                cont = cont+1
    if (cont!=0) :
        return(True)
    else :
        return(False)


#escreva o programa principal
#ENTRADA
n = int(input('Digite a quantidade de valores : '))
a = []
b = []
c = []
#PROCESSAMENTO
for i in range (0,n,1) :
    valora = float(input('Digite o valor para a lista a : '))
    a.append (valora)
for i in range (0,n,1) :
    valorb = float(input('Digite o valor para a lista b : '))
    b.append (valorb)
for i in range (0,n,1) :
    valorc = float(input('Digite o valor para a lista c : '))
    c.append (valorc)
#SAIDA
if crescente(a) :
    print('S')
else :
    print('N')
if decrescente(a) :
    print('S')
else :
    print('N')
if iguais(a) :
    print('S')
else :
    print('N')
if crescente(b) :
    print('S')
else :
    print('N')
if decrescente(b) :
    print('S')
else :
    print('N')
if iguais(b) :
    print('S')
else :
    print('N')
if crescente(c) :
    print('S')
else :
    print('N')
if decrescente(c) :
    print('S')
else :
    print('N')
if iguais(c) :
    print('S')
else :
    print('N')

    

