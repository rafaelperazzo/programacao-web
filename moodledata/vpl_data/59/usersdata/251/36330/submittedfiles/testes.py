# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
investimento = float (input('Digite o valor do investimento inicial: '))
taxa = float (input('Digite o valor da taxa anual (em decimais): '))
renda = (investimento*taxa)
for i in range (1,10+1,1):
    print('%.2f'%renda)
    investimento=renda
