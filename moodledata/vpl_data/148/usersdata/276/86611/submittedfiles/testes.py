# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

investimento = float(input('Digite o valor de reais: '))
taxadecrescimento = float(input('Digite o valor da taxa de crescimento: '))

for i in range (0, 10, 1):
    investimento = investimento*taxadecrescimento
    print(investimento)
    i = i + 1