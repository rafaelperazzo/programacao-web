# -*- coding: utf-8 -*-
n=int(input("Digite a quantidade de salas: "))
v=[]
for i in range(0,n,1):
    a.append(int(input("Digite o valor de vidas: ")))
print(a)
a=int(input("Digite a porta de entrada: "))
b=int(input("Digite a porta de saida: "))
soma=0
if a<b:
    for i in range(a,b+1,1):
        soma=soma+v[i]
for a>b:
    for i in range(b,a+1,1):
        soma=soma+v[i]
print(soma)