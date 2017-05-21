# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
v=float(input('Digite a quantia por hora:'))
h=float(input('Digite a quantidade de horas trabalhadas:'))
sb=(v*h)
i=(v*h)*(8/100)
s=(v*h)*(5/100)
sl=(v*h)-(v*h)*(24/100)
print('Salário bruto: %.1f' %sb)
print('INSS: %.1f' %i)
print('Sindicato: %.1f' %s)
print('Salario liquido: %.1f' %sl)