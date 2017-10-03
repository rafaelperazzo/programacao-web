# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
data1 = [0, 0, 0]
data2 = [0, 0, 0]
data1[0] = int(input('Dia 1: '))
data1[0] = int(input('Mes 1: '))
data1[0] = int(input('Ano 1: '))
data2[0] = int(input('Dia 1: '))
data2[0] = int(input('Mes 1: '))
data2[0] = int(input('Ano 1: '))

if (data1 == data2):
    print('iguais')
elif (data1 > data2):
    print('Data 1')
else:
    print('Data 2')


"""
------------------ Exercício 2 proposto pela monitoria
num = int(input('Número de competidores: '))
nm = float(input('Nota mínima para aprovação: '))
print('\n')
i = 1
total = 0
while i<=num:
    print('- - Candidato %d - - ' % i)
    n1 = float(input('Insira a nota 1: '))
    n2 = float(input('Insira a nota 2: '))
    if ((n1+n2)>= nm):
        total += 1
    i += 1
    print('\n')
print('%d' % total)


------------------ Exercício 1 proposto pela monitoria
i = 1
total = 0
limanterior = 0
np = int(input('Informe o número de pessoas: '))
while i<=np:
    atual = int(input('Instante: '))
    total = total+10
    if atual<(limanterior):
        total = total - (limanterior - atual)
    limanterior = atual +10
    i += 1
print (total)"""