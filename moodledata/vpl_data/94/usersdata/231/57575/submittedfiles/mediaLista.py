# -*- coding: utf-8 -*-

def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
def primeiro(lista):
    for i in range(0,len(lista),1):
        if i==0:
            m=lista[i]
    return m
def ultimo(lista):
    for i in range(0,len(lista),1):
        if i==lista[-1]:
            k=lista[i]
    return k
    
n=int(input('n:'))
a=[]
for i in range(0,n,1):
    numero=int(input('numero:'))
    a.append(numero)
print(primeiro(a))
print(ultimo(a))
print(media(a))
print(a)














