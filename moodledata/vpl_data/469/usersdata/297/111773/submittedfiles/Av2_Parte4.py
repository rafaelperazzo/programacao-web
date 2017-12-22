# -*- coding: utf-8 -*-
m=int(input('digite o numero de ruas que tera o sentido norte sul: '))
while m<2 or m>1000:
    m=int(input('digite o numero de ruas que tera o sentido norte sul: '))
n=int(input('digite o numero de ruas que tera o sentido leste oeste: '))
while n<2 or n>1000:
    n=int(input('digite o numero de ruas que tera o sentido leste oeste: '))
matriz=[]
for i in range(0,m,1):
    linha=[]
    for j in range(0,n,1):
        a=int(input('digite o valor em milhoes da quadra: '))
        if a>=1 and a<=100:
            linha.append(a)
    matriz.append(linha)
menor_valor=1000000
for k in range(0,m,1):
    soma=0
    for r in range(0,n,1):
        soma=soma+matriz[k][r]
    if soma<menor_valor:
        menor_valor=soma
print(menor_valor)