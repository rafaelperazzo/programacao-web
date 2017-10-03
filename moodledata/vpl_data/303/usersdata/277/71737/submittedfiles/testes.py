# -*- coding: utf-8 -*-
# Entrada
a = int(input('Que horas são? [0-23] '))
# Processamento e saída
if a < 0 or a > 23:
    print('Hora invalida')
else:
    if a > 3 and a < 12:
        print('Bom dia')
    elif a >= 12 and a < 18:
        print('Boa tarde')
    else:
        print('Boa noite')

































"""
# ENTRADA
x = int(input('digite um numero inteiro qualquer: '))
# PROCESSAMENTO
teste1 = x > 50
teste2 = (x > 0) and (x <= 100)
# SAIDA
print("O numero " + str(x) + " é maior do que 50: " + str(teste1))
print("O numero " + str(x) + " está entre 0 e 100: " + str(teste2))
print("5"+"2")
"""
