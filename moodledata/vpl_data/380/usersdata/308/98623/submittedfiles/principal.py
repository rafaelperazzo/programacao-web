import random
x = '0123456789'
teste = ''
try:
    teste = 'teste1'
    x[10] = '10'
    teste = 'teste2'
except: 
    x = 10
finally:
    print('%s - %s' % (x, teste))


'''
texto = "0123456789"
print(texto[2:8])
print(texto[:8])
print(texto[4:])
jogada = '0 2'
print('\nLinha: '+jogada[0])
print('Coluna: '+jogada[2])


from minha_bib import *
from random import randint
import time
agora = str(date)
print(agora)
a = 10
b = 10
print(id(a))
print(id(b))
a = 11
print(id(a))
print(id(b))
'''