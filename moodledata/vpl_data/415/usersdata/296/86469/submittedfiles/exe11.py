# -*- coding: utf-8 -*-
n = int(input("Digite um número: "))
soma = 0
i = 1
while i <= n:
    if 10000000 <= n <= 90000000:
        soma = soma + i
        i = i + 1
        print (soma)
    else:
        print("NAO SEI")