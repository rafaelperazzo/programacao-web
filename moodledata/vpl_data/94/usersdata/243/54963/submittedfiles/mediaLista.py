# -*- coding: utf-8 -*-
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
    
n=int(input('digite a quantidade de numeros:'))
a=[]
for i in range(0,n,1):
    valor=int(input('digite o valor:'))
    a.append(valor)
    
print(a[0])
print(a[i])
print(media(a))
print(lista)


