# -*- coding: utf-8 -*-
n=int(input("digite o numero:"))
soma=0
aux=n
while(aux>0):
    soma+=aux%10
    aux=int(aux/10)
    print(soma)