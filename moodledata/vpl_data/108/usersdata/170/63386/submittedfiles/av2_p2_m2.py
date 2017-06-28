# -*- coding: utf-8 -*-
def jogo(lista,e,s):
    soma=0
    if s>=e:
        for i in range (e,s+1,1):
            soma=soma+lista[i]
    else:
        for i in range (e,s-1,1):
            soma=soma+lista[i]
    return soma
n=int(input('Digite n:'))
lista=[]
for i in range (0,n,1):
    valor=int(input('Quantidade de vidas em cada sala:'))
    lista.append (valor)
e=int(input('Entrada:'))
s=int(input('Saida:'))
print(jogo(lista,e,s))

