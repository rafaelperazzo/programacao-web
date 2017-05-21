# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
v=float(input('Digite a quantia por hora:'))
h=float(input('Digite a quantidade de horas trabalhadas:'))
sb=(v*h)
i=(v*h)*0,08
s=(v*h)*0,05
sl=(v*h)-(v*h)*0,24
print('Salário bruto: %.1f' %sb)
print('INSS: %.1f' %i)
print('Sindicato: %.1f' %s)
print('Salario liquido: %.1f' %sl)