# -*- coding: utf-8 -*-
from __future__ import division

investimentoInicial=input('Digite o valor do investimento inicial:')
taxaDeCrescimento=input('Digite o valor da taxa de crescimento percentual:')

investimento1=investimentoInicial+taxaDeCrescimento*(investimentoInicial)
investimento2=investimento1+taxaDeCrescimento*(investimento1)
investimento3=investimento2+taxaDeCrescimento*(investimento2)
investimento4=investimento3+taxaDeCrescimento*(investimento3)
investimento5=investimento4+taxaDeCrescimento*(investimento4)
investimento6=investimento5+taxaDeCrescimento*(investimento5)
investimento7=investimento6+taxaDeCrescimento*(investimento6)
investimento8=investimento7+taxaDeCrescimento*(investimento7)
investimento9=investimento8+taxaDeCrescimento*(investimento8)
investimento10=investimento9+taxaDeCrescimento*(investimento9)

print('O valor do investimento do 1 ano será=%.2f:' %investimento1)
print('O valor do investimento do 2 ano será=%.2f:' %investimento2)
print('O valor do investimento do 3 ano será=%.2f:' %investimento3)
print('O valor do investimento do 4 ano será=%.2f:' %investimento4)
print('O valor do investimento do 5 ano será=%.2f:' %investimento5)
print('O valor do investimento do 6 ano será=%.2f:' %investimento6)
print('O valor do investimento do 7 ano será=%.2f:' %investimento7)
print('O valor do investimento do 8 ano será=%.2f:' %investimento8)
print('O valor do investimento do 9 ano será=%.2f:' %investimento9)
print('O valor do investimento do 10 ano será=%.2f:' %investimento10)


