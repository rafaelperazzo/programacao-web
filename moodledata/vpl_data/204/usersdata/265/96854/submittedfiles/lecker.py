# -*- coding: utf-8 -*-
def lecker(lista):
    cont=0
    cont1=0
    cont2=0
    cont3=0
    for i in range (0,len(lista),1):
        if i==0:
            if a[i]>a[i+1]:
                cont1=cont1+1
        elif i==(len(lista)-1):
            if a[i]>a[i-1]:
                cont2=cont2+1
        else:
            if (a[i]>a[i+1] and a[i]>a[i-1]):
                cont3=cont3+1
    cont=cont1+cont2+cont3
    if cont==1:
        return(True)
    else:
        return(False)
n=int(input('digite a quantidade de valores das listas: '))
a=[]
b=[]
for i in range (0,n,1):
    valorA=int(input('digite os termos da lista a: '))
    a.append(valorA)
for i in range (0,n,1):
    valorB=int(input('digite os termos da lista b: '))
    b.append(valorB)
if lista(a)==True:
    print('S')
if lista(a)==False:
    print('N')
if lista(b)==True:
    print('S')
if lista(b)==False:
    print('N')
    