#from minha_bib import *
# -*- coding: utf-8 -*-

# inicializando lista de notas
notas = []

# lendo cinco notas do usuário
for i in range(0,5,1):
    notas.append(float(input('Digite a nota%d: ' % (i+1))))

# mostrando toda a lista de notas
print(notas)