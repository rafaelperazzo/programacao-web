# -*- coding: utf-8 -*-

def media(a):
    soma = 0
    for i in range(0,len(a),1):
        soma = soma + a[i]
    resultado = soma/len(a)
    return resultado

def desvio(lista,media):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+(lista[i]-media)**2
    desvio=(soma/(len(lista)-1))**0.5
    return desvio
    
    
n=int(input('Quantidade de elementos das listas:'))
a=[]

for i in range (0,n,1):
    valor=float(input('Valor de a:'))
    a.append(valor)

b=[]

for i in range (0,n,1):
    valor=float(input('Valor de b:'))
    b.append(valor)


print('%.2f'%media(a))
print('%.2f'%desvio(a,media(a)))
print('%.2f'%media(b))
print('%.2f'%desvio(b,media(b)))