# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de valores: '))
lista = []
for i in range (1,n+1,1):
    valor = input('Digite o valor '+str(i)+': ')
    lista.append(valor)
print(len(lista))    


