# -*- coding: utf-8 -*-
n = int(input("Digite um número: "))
soma = 0
i = n
while i > 0:
    if 10000000 <= n <= 90000000:
        soma = i%10
        i = int(i/10)
        print (soma)
    else:
        print("NAO SEI")