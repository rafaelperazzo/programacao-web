# -*- coding: utf-8 -*-
n = int(inpru("Digite um valor:"))
numeros = []
soma1=0
soma2=0
a = 0 
b = 0
for i in range (0,n,1):
    numeros.append(int(input("Digite o número%.d: " %(i+1))))
for i in range(0,n,1):
    if numeros[i]%2!=0:
        soma1+=numeros[i]
        a+=1
print(soma1)
for i in range (0,n,1):
    if numeros[i]%2==0:
        soma2+=numeros[i]
        b+=1
print(soma2)
print(a)
print(b)
print(numeros)