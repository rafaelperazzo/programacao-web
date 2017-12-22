# -*- coding: utf-8 -*-
matriz=[]
m=int(input('Digite o valor de m: '))
while 2> m or m>1000:
    m=int(input('Digite o valor de m: '))
n=int(input('Digite o valor de n: '))
while 2>n or n>1000:
    n=int(input('Digite o valor de n: '))
    for i in range(0,n-1,1):
        linha=[]
        for j in range( 0,n-1n1):
            linha.append(int(input('Digite o valor da quadra: ')))
        matriz.append(linha)
print(matriz)