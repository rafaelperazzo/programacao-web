# -*- coding: utf-8 -*-
n = int(input("Digite um número: "))
soma = 0
while n > 0:
    if 10000000 <= n <= 90000000:
        resto = n%10000000
        n = (n - resto)/10000000
        print(n)
   
    