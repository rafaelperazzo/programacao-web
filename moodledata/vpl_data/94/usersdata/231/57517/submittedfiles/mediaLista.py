# -*- coding: utf-8 -*-

def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
n=int(input('n:'))
a=[]
for i in range(0,n,1):
    numero=int(input('numero:'))
    a.append(numero)
    if i==0:
        print(i)
print(media(a))
print(a)













