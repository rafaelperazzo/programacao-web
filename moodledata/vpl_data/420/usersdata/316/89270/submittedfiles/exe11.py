# -*- coding: utf-8 -*-
n=int(input("Digite um número com oito algarismos:"))
soma=0
while n<100000000 and n>9999999:
    resto=(n%10000000)
    n=(n-resto)/10000000
    soma=soma+resto
print("a soma dos numeros é: ", n)