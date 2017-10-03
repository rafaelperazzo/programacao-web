# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
c= float(input('Custo de fábrica de um carro: '))
pd= (c * 28)/100
pi= (c * 45)/100
cf= c + pd + pi
print('R$%.2f' % cf)