# -*- coding: utf-8 -*-
n=int(input('n:'))
lista=[]
soma1=0
soma2=0
for i in range(0,n,1):
    numero=float(input('numero:'))
    lista.append(numero)
print('%.2f' % lista[0])
print('%.2f' % lista[len(lista)-1])
for i in range(0,len(lista),1):
    soma2=soma2+lista[i]
media=soma2/len(lista)
print('%.2f' % media)
print(lista)




