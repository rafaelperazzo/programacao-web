# -*- coding: utf-8 -*-

n = int(input('Digite o vão: '))
lista = []
for i in range(0,n,1):
    lista.append(int(input('Digite a altura: ')))
'''    
for i in range(0,len(lista),1):
    soma=0
    if lista[0]>=lista[i]:
        soma = soma+(lista[0]-lista[i])
    else:
        break
    print(soma)
'''
for i in range(0,n,1):
    cont = 0
    if lista[0] < lista[i]:
        cont = cont+1
        break
if cont == 0:
    j = 0
    if lista[0] == lista[i]:
        j=i
    cont1=0
    for i in range(1,j,1):
        cont1 = cont1 + 1
    print(cont1)
if cont1 == 1:
    for i in range(1,n,1):
        if lista[i] > lista[i+1]:
            t = i
            

