# -*- coding: utf-8 -*-
a=int(input("Digite um número: "))
i=0
soma=0
b=100000000
c=7
while b!=1:
    i=a//10**c
    soma=soma+i
    b=b/10
    a=a-(i*10**c)
    c=c-1
print(soma)