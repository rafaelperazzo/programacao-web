# -*- coding: utf-8 -*-
def vidas(a):
    soma=0
    for i in range(f,g,1):
        soma=soma+a[i]
    return soma

n=int(input('tamanho do jogo: '))
lista=[ ]
for i in range(1,n+1,1):
    valor=float(input('vidas no quarto: '))
    lista.append(valor)
f=int(input('porta de entrada: '))
g=int(input('porta de saida: '))

print(vidas(lista))