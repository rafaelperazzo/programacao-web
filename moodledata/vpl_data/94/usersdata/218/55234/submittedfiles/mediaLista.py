# -*- coding: utf-8 -*-
def media (lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
    soma=(soma/len(lista))
    return soma
n= int(input('digite o numero de elementos da lista:'))
a=[]
for i in range (0,n,1):
    numero=int(input('digite o elemento da lista:'))
    a.append(numero)
print('%.2f'%a[0])
print('%.2f'%a[(n-1)])
valor=media (a)
print('%.2f'%valor)
print('%.1f'%a)