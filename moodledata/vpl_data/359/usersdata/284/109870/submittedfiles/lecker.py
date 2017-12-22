# -*- coding: utf-8 -*-
lista=[]
lista2=[]
n=(int(input('digite o numero de termos: ')))
for i in range(0,n,1):
    lista.append(int(input('digite o numero da lista1: ')))

#lecker
#extremidades
cont=0
if lista[0]>lista[1]:
    cont=cont+1

cont1=0
if lista[n-1]>lista[n-2]:
    cont1=cont1+1

#centro
cont2=0
for i in range(1,n-1,1):
    if lista[i]>lista[i-1] and lista[i]>lista[i+1]:
        cont2=cont2+1

###########lista2
for i in range(0,n,1):
    lista2.append(int(input('digite o numero da lista2: ')))

#lecker
#extremidades
cont3=0
if lista2[0]>lista2[1]:
    cont3=cont3+1

cont4=0
if lista2[n-1]>lista2[n-2]:
    cont4=cont4+1

#centro
cont5=0
for i in range(1,n-1,1):
    if lista2[i]>lista2[i-1] and lista2[i]>lista2[i+1]:
        cont5=cont5+1

#verificação
if (cont+cont1+cont2)==1:
    print('S')
else:
    print('N')
if (cont3+cont4+cont5)==1:
    print('S')
else:
    print('N')




















