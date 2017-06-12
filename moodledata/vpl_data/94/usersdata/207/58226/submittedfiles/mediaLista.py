# -*- coding: utf-8 -*-

def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
n=int(input('n:'))
a=[]
x=0
z=0
for i in range(0,n,1):
    numero=int(input('numero:'))
    a.append(numero)
    if i==0:
        x=numero
    if i==(n-1):
        z=numero
print('%.2f'%x)
print('%.2f'%z)
print('%.2f'%media(a))
print(a)

