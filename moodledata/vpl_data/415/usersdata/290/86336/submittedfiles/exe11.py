# -*- coding: utf-8 -*-
a=int(input("Digite um número: "))
i=0
soma=0
b=100000000
while a<b:
    i=a//10
    soma=soma+i
    b=b/10
print(soma)