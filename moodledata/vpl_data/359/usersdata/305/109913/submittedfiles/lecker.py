# -*- coding: utf-8 -*-
n = int(input('Digite o valor da lista: '))
lista_1 = []
lista_2 = []
for i in range (0,n,1):
    lista_1.append(int(input('Digite o valor %d da lista 1: ' %(i + 1))))
for i in range (0,n,1):
    lista_2.append(int(input('Digite o valor %d da lista 2: ' %(i + 1))))
    
cont1 = 0
for i in range (1,n,1):
    if lista_1[i] > lista_1[i - 1] and lista_1[[1] > lista_1[i + 1]:
        cont1 = cont1 + 1
if lista_1[0] > lista_1[1]:
    cont1 = cont1 + 1
if lista_1[n - 1] > lista_1[n - 2]:
    cont1 = cont1 + 1
    
cont2 = 0
for i in range (1,n,1):
    if lista_2[i] > lista_2[i - 1] and lista_2[i] > lista_2[i + 1]:
        cont2 = cont2 + 1
if lista_2[0] > lista_2[1]:
    cont2 = cont2 + 1
if lista_2[n - 1] > lista_2[n - 2]:
    cont2 = cont2 + 1
if cont1 == 1 and cont2 == 1:
    print('S')
    print('S')
elif cont1 == 1 and cont2 != 1:
    print('S')
    print('N')
elif cont1 != 1 and cont2 == 1:
    print('N')
    print('S')
else:
    print('N')
    print('N')

