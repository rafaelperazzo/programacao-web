# -*- coding: utf-8 -*-
n=int(input('Digite o número de termos: '))
lista1=[]
lista2=[]
for i in range (0,n,1):
    lista1.append(int(input('Digite o valor %d da lista 1: ' %(i+1))))
for i in range (0,n,1):
    lista2.append(int(input('Digite o valor %d da lista 2: ' %(i+1))))
cont1=0
for i in range (1,n,1):
    if lista1[i]>lista1[i-1] and lista1[i]> lista1[i+1]:
        cont1 = cont1+1
if lista1[0]> lista1[1]:
    cont1=cont1+1
if lista1[n-1] > lista1[n-2]:
    cont1=cont1+1
    
cont2=0
for i in range (1,n,1):
    if lista2[i]>lista2[i-1] and lista2[i]> lista2[i+1]:
        cont2 = cont2+1
if lista2[0]> lista2[1]:
    cont2=cont2+1
if lista2[n-1] > lista2[n-2]:
    cont2=cont2+1
if cont1==1 and cont2==1:
    print('S')
    print('S')
elif cont1==1 and cont2!=1:
    print('S')
    print('N')
elif cont1!=1 and cont2==1:
    print('N')
    print('S')
else:
    print('N')
    print('N')
    
    
    
    
    
    