# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

investimento = float(input('Digite o valor de reais: '))
taxadecrescimento = float(input('Digite o valor da taxa de crescimento: '))

investimento1 = investimento

for i in range (0, 10, 1):
    investimento = investimentoinvestimento*taxadecrescimento
    print(investimento1 + investimento)
    i = i + 1