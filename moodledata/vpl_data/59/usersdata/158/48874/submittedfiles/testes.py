# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
s=float(input('salário mensal:'))
p=float(input('percentual de ajuste:'))
ns=s+((p/100)*s)
print('o valor do novo salário é: %.2f' %ns)
