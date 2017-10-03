# -*- coding: utf-8 -*-
n = int(input('DIgite um número de 8 algarismos: '))
if n > 9999999:
    soma = 0
    while (n != 0):
        resto = n%10
        n = (n-resto)//10
        soma = soma + resto
    print(soma)
else:
    print('NÃO SEI')
