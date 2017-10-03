# -*- coding: utf-8 -*-


#COMECE SEU CODIGO AQUI
valor=float(input('Digite o valor do capital inicial:'))
taxa=float(input('Digite o valor da taxa anual:'))
investimento=valor
ano=1
while ano<=10:
    investimento=investimento+investimento*taxa
    print('%.2f'%investimento)
    ano=ano+1