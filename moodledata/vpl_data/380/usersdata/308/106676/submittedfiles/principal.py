notas = []
nota = 1
while True:
    valor = input('Informe a nota %d: ' % nota)
    if valor == 'n':
        break
    notas.append(float(valor))
    nota = nota + 1
print(sum(notas)/len(notas))
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