# -*- coding: utf-8 -*-
def somadigitos(num):
    s=0
    while num>0:
        s=s+num%10
        num=num//10
    return s
    
n=int(input("digite o numero:"))
soma=0
while n>0:
    num=int(input("numero:"))
    soma=soma+somadigitos(num)
    n=n-1
    print(soma)
