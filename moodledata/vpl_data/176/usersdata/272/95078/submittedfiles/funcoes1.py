# -*- coding: utf-8 -*-


def crescente (lista):
    #escreva o código da função crescente aqui
    cont=0
    for i in range (0,len(lista),1):
        if (i==0):
            if (lista[i]<lista[i+1]):
                cont=cont+1
        elif (i==(len(lista)-1)):
            if (lista[i-1]<lista[i]):
                cont=cont+1
        else:
            if (lista[i]<lista[i+1]):
                cont=cont+1
    if (cont==len(lista)):
        return(True)
    else:
        return(False)
        
#escreva as demais funções
def decrescente (lista):
    cont=0
    for i in range (0,len(lista),1):
        if (i==0):
            if (a[i]>a[i+1]):
                cont=cont+1
        elif (i==(len(lista)-1)):
            if (a[i-1]>a[i]):
                cont=cont+1
        else:
            if (a[i]>a[i+1]):
                cont=cont+1
    if (cont==len(lista)):
        return(True)
    else:
        return(False)

def consecutivo_igual (lista):
    cont=0
    for i in range (0,len(lista),1):
        if (i==0):
            if (a[i]==a[i+1]):
                cont=cont+1
        elif (i==(len(lista)-1)):
            if (a[i-1]==a[i]):
                cont=cont+1
        else:
            if (a[i]==a[i+1]):
                cont=cont+1
    if (cont!=0):
        return(True)
    else:
        return(False)

#escreva o programa principal

n = int(input('Digite o número de elementos das listas: '))
a=[]
b=[]
c=[]

for i in range (0,n,1):
    a.append(int(input('Digite o valor: ')))

for j in range (0,n,1):    
    b.append(int(input('Digite o valor: ')))

for k in range (0,n,1):    
    c.append(int(input('Digite o valor: ')))
    

if (crescente(a)):
    print('S')
if (not crescente(a)):
    print('N')

if (decrescente(a)):
    print('S')
if (not decrescente(a)):
    print('N')

if (consecutivo_igual(a)):
    print('S')
if (not consecutivo_igual(a)):
    print('N')


if (crescente(b)):
    print('S')
if (not crescente(b)):
    print('N')

if (decrescente(b)):
    print('S')
if (not decrescente(b)):
    print('N')

if (consecutivo_igual(b)):
    print('S')
if (not consecutivo_igual(b)):
    print('N')


if (crescente(c)):
    print('S')
if (not crescente(c)):
    print('N')

if (decrescente(c)):
    print('S')
if (not decrescente(c)):
    print('N')

if (consecutivo_igual(c)):
    print('S')
if (not consecutivo_igual(c)):
    print('N')
