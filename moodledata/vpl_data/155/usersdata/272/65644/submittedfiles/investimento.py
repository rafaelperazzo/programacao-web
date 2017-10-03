# -*- coding: utf-8 -*-
from __future__ import division

#COMECE SEU CODIGO AQUI

investimento= float(input('Digite o valor do investimento inicial:'))
taxa= float(input('Digite o valor da taxa anual:'))

investimento1= investimento+(taxa*investimento)
investimento2= investimento1+(taxa*investimento1)
investimento3= investimento2+(taxa*investimento2)
investimento4= investimento3+(taxa*investimento3)
investimento5= investimento4+(taxa*investimento4)
investimento6= investimento5+(taxa*investimento5)
investimento7= investimento6+(taxa*investimento6)
investimento8= investimento7+(taxa*investimento7)
investimento9= investimento8+(taxa*investimento8)
investimentofinal= investimento9+(taxa*investimento9)

print('%.2f' %investimento1)
print('%.2f' %investimento2)
print('%.2f' %investimento3)
print('%.2f' %investimento4)
print('%.2f' %investimento5)
print('%.2f' %investimento6)
print('%.2f' %investimento7)
print('%.2f' %investimento8)
print('%.2f' %investimento9)
print('%.2f' %investimentofinal)

