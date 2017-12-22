# -*- coding: utf-8 -*-

def intervalo (p):
    periodo=10
    for i in range(1,len(p),1):
        periodo=periodo+(p[i]-p[i-1])
    return(periodo)

n=int(input('Quantidade de pessoas: '))
lista=[ ]

for i in range(0,n,1):
    lista.append(int(input('Instante que a pessoa passa: ')))
 print(intervalo(lista))