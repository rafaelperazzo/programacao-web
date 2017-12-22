import random
import copy
def foo():
    return 'teste'
x = ['foo', foo()]
y = x
z = list(x)
q = copy.copy(x)
w = copy.deepcopy(x)
x.append(4)
print(y)
print(z)
print(q)
print(w)


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