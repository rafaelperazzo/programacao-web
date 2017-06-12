# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite n:'))
for i in range(0,n,1):
    a=float(input('digite cada elemento:'))
    lista.append(a)
soma=0
for i in range(0,len(lista),1):
    soma=soma+(lista[i])
media=soma/n
print('Primeiro elemento: %.2f'%lista[0])
print('Último elemento: %.2f'%lista[n-1])
print('A média é: %.2f'%media)
print(lista)
    


