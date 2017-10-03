# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
s= float(input('Salário mensal atual: '))
p= float(input('Reajuste em porcentagem: '))

a= (s * p)/100
ns= s + a
print('R$%.2f' % ns)