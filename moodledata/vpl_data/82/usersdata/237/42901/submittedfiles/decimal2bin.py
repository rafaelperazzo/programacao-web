# -*- coding: utf-8 -*-
d=int(input("Digite o número binario: "))
i=0
soma=0
a=d%10
while a!=0:
    a=d%10
    soma=soma+(a*(2**i))
    d=d//10
    i=i+1
print(soma)
