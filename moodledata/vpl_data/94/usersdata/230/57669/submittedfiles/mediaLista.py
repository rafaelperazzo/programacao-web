# -*- coding: utf-8 -*-
def media(a):
    soma=0
    for i in range (0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return media
a=[]   
n=int(input('Digite quantidade de valores: '))
for i in range (1,n+1,1):
    numero=float(input('Digite valor: '))
    a.append(numero)
lista = a[0]
print(lista)
print('%.2f' %len(a))
print('%.2f' %media(a))
print(a)
