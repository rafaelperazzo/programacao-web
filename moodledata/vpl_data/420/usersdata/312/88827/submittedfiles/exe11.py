# -*- coding: utf-8 -*-
n=int(input("digite o numero:"))
soma=0
while(n!=0):
    resto=n%10
    n=(n-resto)
    soma=soma+resto
    print(soma)