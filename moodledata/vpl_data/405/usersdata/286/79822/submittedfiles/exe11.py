# -*- coding: utf-8 -*-
valor = int(input('Quanto você deseja sacar? '))

a = valor//50

b = (valor%50)//20

c =  (valor - ((a*50) + (b*20)))//10

d = (valor - ((a*50) + (b*20) + (c*10)))//5

e = (valor - ((a*50) + (b*20) + (c*10) + (d*5)))//2

print('\n%i' % a)
print('\n%i' % b)
print('\n%i' % c)
print('\n%i' % d)
print('\n%i' % e)
