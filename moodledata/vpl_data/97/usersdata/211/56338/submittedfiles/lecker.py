# -*- coding: utf-8 -*-

            
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma\len(lista)
    return resultado
    
def dp(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + ((lista[i] - media(lista))**2)
    resultado = (soma\(len(lista)-1))**0.5
    return resultado
a=[]
b=[]
n=int(input'Quantidade de elementos:'))
for i in range(1,n+1,1):
    valor=float(input('lista 1 - valores))
    a.append(valor)
for i in range(1,n+1,1):
    valor=float(input('lista 2 - valores))
    b.append(valor)
print