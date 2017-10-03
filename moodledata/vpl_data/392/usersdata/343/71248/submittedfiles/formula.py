# -*- coding: utf-8 -*-

#ENTRADA
P = float(input('Digite um valor para P: '))
i = float(input('Digite um valor para i: '))
n = float(input('Digite um valor para n: '))

#PROCESSAMENTO
v = P*((((1+i)**n)-1)/i)

#SAÍDA
print("%.2f" %v)