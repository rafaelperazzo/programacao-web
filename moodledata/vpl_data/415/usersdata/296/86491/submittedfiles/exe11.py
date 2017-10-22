# -*- coding: utf-8 -*-
n = int(input("Digite um número: "))
soma = 0
while n > 0:
    if 10000000 <= n <= 90000000:
        soma = soma + n%100000000
        n//=10
        print(soma)
    else:
        print("NAO SEI")
    