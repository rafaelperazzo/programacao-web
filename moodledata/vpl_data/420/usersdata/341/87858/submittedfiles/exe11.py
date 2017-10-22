# -*- coding: utf-8 -*-

n = int(input("Digite um número de oito algarismos: "))
soma = 0
tempo = 10000000
if n < 100000000 and n > 9999999:
    for i in range (0,8,1):
        soma = soma + (n//tempo)
        n = n%tempo
        tempo = tempo/10
    print('%d' %soma)
else: 
    print('NAO SEI')

