# -*- coding: utf-8 -*-
n = input('Digite o número: ')
lista = []
for i in range (1,n+1,1):
    valor = input('Digite o valor '+str(i)+': ')
    lista.append(valor)
print(len(lista))    


