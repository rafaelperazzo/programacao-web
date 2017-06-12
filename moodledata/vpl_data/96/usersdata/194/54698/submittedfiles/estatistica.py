# -*- coding: utf-8 -*-


def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    resultado=(soma/(len(lista)-1))**0.5
    return(resultado)
    
n=int(input('digite a quantidade de elementos da lista:'))
a=[]
for i in range(0,n,1):
    valor1=int(input('digite os elementos da lista 1:'))
    a.append(valor1)
b=[]
for i in range(0,n,1):
    valor2=int(input('digite os elementos da lista 2:'))
    b.append(valor2)

print('%.2f'%media(a))
print('%.2f'%desvio(a))
print('%.2f'%media(b))
print('%.2f'%desvio(b))