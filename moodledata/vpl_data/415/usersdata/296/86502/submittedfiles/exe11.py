# -*- coding: utf-8 -*-
n = int(input("Digite um número: "))
soma = 0
while (n > 0):
    if 10000000 <= n <= 90000000:
        resto = n%10
        n = (n-resto)/10
        soma = soma + resto
            print(soma)
   
    