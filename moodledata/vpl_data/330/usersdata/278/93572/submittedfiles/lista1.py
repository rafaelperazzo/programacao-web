# -*- coding: utf-8 -*-
n = int(input("Digite um valor: "))
numeros = []
soma1=0
soma2=0
for i in range (0,n,1):
    numeros.append(int(input("Digite o número%.d: " %(i+1))))
for i in range (0,n,1):
    if numeros[i]%2!=0:
        soma1+=numeros[i]
print(soma1)
for i in range (0,n,1):
    if numeros[i]%2==0:
        soma2+=numeros[i]
print(soma2)
for i in range (0,n,1):
    if numeros[i]%2==0:
        numeros.remove()
print(len(numeros))