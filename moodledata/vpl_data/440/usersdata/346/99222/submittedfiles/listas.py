# -*- coding: utf-8 -*-
def comp(a):
    maior_altura= 0
    for i in range(0,len(a)-1,1):
        altura= abs(a[i])-abs(a[i+1])
        if abs(altura) > maior_altura:
            maior_altura= abs(altura)
    return maior_altura


n= int(input('Digite o valor de n: '))
lista= []
for i in range(0,n,1):
    lista.append(int(input('Digite um valor: ')))

print(maior_altura(lista))