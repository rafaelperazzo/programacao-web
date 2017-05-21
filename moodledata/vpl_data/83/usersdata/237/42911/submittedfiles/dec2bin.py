# -*- coding: utf-8 -*-
d=int(input("Digite o numero de base decimal: "))
i=0
soma=0
while d>0:
    m=d%2
    soma=soma+m*(10**i)
    d=d//2
    i=i+1
print(soma)
