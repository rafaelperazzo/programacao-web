# -*- coding: utf-8 -*-


def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
    
def dp(lista):
    soma=0
    for i in range(1,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    resultado=(soma/(len(lista)-1))**1/2
    return resultado
n=int(input('digite o numero de elementos :'))
lista a=[]
lista b=[]
for i in range(1,n+1,1):
    valor1=int(input('digite o valor dos elementos da primeira lista :'))
    lista a.append(valor1)
for i in range(1,n+1,1):
    valor2=int(input('digite o valor dos elementos da segunda lista :'))
    lista b.append(valor2)
print('%.2f'%media(lista a))
print('%.2f'%dp(lista a))
print('%.2f'%media(lista b))
print('%.2f'%dp(lista b))    
    
        












    