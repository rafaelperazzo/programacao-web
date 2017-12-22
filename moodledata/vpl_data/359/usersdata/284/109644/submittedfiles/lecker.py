# -*- coding: utf-8 -*-
n=(int(input('digite a quantidade de termos: ')))
lista=[]

#termos
for i in range(0,n,1):
    lista.append(int(input('digite o valor da lista: ')))

#lecker

#extremidades
cont=0
if lista[1]>lista[0] and lista[1]>lista[2]:
    cont=cont+1
cont1=0
if lista[n-2]>lista[n-1] and lista[n-2]>lista[n-3]:
    cont1=cont1+1

#centro
cont2=0
for i in range(1,n-1,1):
    if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
        cont2=cont2+1

############################################lista2
lista2=[]

#termos
for i in range(0,n,1):
    lista2.append(int(input('digite o valor da lista2: ')))

#lecker

#extremidades
cont3=0
if lista2[1]>lista2[0] and lista2[1]>lista2[2]:
    cont3=cont+1
cont4=0
if lista2[n-2]>lista2[n-1] and lista2[n-2]>lista2[n-3]:
    cont3=cont3+1

#centro
cont5=0
for i in range(1,n-1,1):
    if lista2[i]>lista2[i+1] and lista2[i]>lista2[i-1]:
        cont5=cont5+1

#######################verificação
if cont==0 or cont1==0 or cont2==0:
    print('S')
else:
    print('n')
if cont3==0 or cont4==0 or cont5==0:
    print('S')
else:
    print('n')

















