# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
valor = float(input('Digite o valor que voce ganha por hora : '))
horas = int(input('Digite o valor de horas que voce trabalha no mes : '))
#PROCESSAMENTO
bruto = (valor*horas)
taxa1 = (bruto*0.08)
taxa2 = (bruto*0.05)
taxa3 = (bruto*0.11)
liquido = (bruto-taxa1-taxa2-taxa3)

#SAIDA
print('O valor bruto é : %.f ' % bruto)
print('O valor do INSS é : %.f ' % taxa1)
print('O valor do sindicato é : %.f ' % taxa2)
print('O valor do salário líquido é : %.f % ' % liquido)

