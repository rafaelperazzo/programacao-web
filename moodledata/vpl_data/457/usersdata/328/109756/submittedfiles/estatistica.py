# -*- coding: utf-8 -*-
def media(lista):
    som=0
    for i in range(0,len(lista),1):
        som=som=lista[i]
    resultado+som/len(lista)
    return resultado
def de(lista,resultado):
    som=0
    for i in range(0,len(lista),1):
        som=som+(( (lista[i]-resultado))**2.0/(len(lista)-1))
    som=som**(1/2.0)
    return soma
m=int(input('Digite listas:'))
n=int(input('Digite o tamanho das listas:'))
matriz=[]
for i in range(m):
    v=[]
    for j in range(n):
        v.append(int(input(Digite valores:')))
    matriz.append(v)
v=[]
for i in range(m):
    v.append(media(matriz[i])
    v.append(dp(matriz[i],v[i*2])
for i in range(m*2):
    print('%.2f'%(v[i]))
   