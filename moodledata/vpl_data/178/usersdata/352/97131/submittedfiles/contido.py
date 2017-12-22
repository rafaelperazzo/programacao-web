# -*- coding: utf-8 -*-


def ocorre (x,lista):
    cont=0
    for i in range(0, len(lista),1):
        if (lissta[i]==x):
            cont=cont+1
    return (cont)















n=int(input('Quantidade de elementos de a: '))
m=int(input('Quantidade de elementos de b: '))

lista_a=[ ]
lista_b=[ ]

for i in range(0,n,1):
    valor=int(input('Valor de a: '))
    lista_a.append(valor)


for i in range(0,n,1):
    valor=int(input('Valor de b: '))
    lista_b.append(valor)