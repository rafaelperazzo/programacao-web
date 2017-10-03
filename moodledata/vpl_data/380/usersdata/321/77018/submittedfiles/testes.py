# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
x= int(input('Quanto ganha por hora: '))
y= int(input('Quantas horas por mês: '))

# Calculos
sb= x * y
ip= 11 / 100 * sb
inss= 8 / 100 * sb
si= 5 / 100 * sb
sl= sb - ip - inss - si

#Saidas
print('a) Salário bruto:%.2f' % sb)
print('b) INSS: %.2f' % inss)
print('c) Sindicato: %.2f' % si)
print('d) Salário liquido: %.2f' % sl)