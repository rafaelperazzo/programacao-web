# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
investimento = float (input('Digite o valor do investimento inicial: '))
taxa = float (input('Digite o valor da taxa anual (em decimais): '))
renda = 0
for i in range (1,10+1,1):
    renda = (investimento+(investimento*taxa))
    investimento=renda
    print('%.2f'%renda)
