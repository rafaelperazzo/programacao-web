# -*- coding: utf-8 -*-


def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
def dp(lista):
    soma=0
    resultado=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    resultado=(soma/(len(lista)-1))**0.5
    return resultado
a=[]
b=[]
n=int(input('escreva o numero de elementos:'))
for i in range(1,n+1,1):
    valor=float(input('escreva o valor dos elementos da primeira lista:'))
    a.append(valor)
for i in range(1,n+1,1):
    valor=float(input('escreva o valor dos elementos da segunda lista:'))
    b.append(valor)
print('%.2f'%media(a))
print('%.2f'%dp(a))
print('%.2f'%media(b))
print('%.2f'%dp(b))
    
        
