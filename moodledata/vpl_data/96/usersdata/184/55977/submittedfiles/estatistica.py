# -*- coding: utf-8 -*-
n=int(input('digite n:'))
lista1=[]
lista2=[]
def media(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma1=soma1+lista[i]
    resultado=soma1/len(lista)
    return (resultado)
def desviopadrao(lista):
    soma2=0
    for i in range(o,len(lista),1):
        soma2=soma2+(lista[i]-media(lista))**(2)
    desviopadrao=(soma2/(n-1))**(0.5)
    return (desviopadrao)
for i in range(0,n,1):
    numero=float(input('digite um numero:'))
    lista1.append(numero)
for i in range(0,n,1):
    numero=float(input('digite numero:'))
    lista2.append(numero)
print('%.2f'%media(lista1))
print('%.2f'%desviopadrao(lista1))
print('%.2f'%media(lista2))
print('%.2f'%desviopadrao(lista2))