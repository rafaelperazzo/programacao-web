# -*- coding: utf-8 -*-

n = int(input("Digite um número de oito algarismos: "))
soma = 0
t = 10000000
if n < 100000000 and n > 9999999:
    for i range (0,8,1):
        soma = soma + (n//t)
        n = n%t
        t = t/10
    print(soma)
else: 
    print('NAO SEI')

