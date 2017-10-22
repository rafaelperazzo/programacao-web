# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

#for i in range(1,10,1):
i=0
while i>10: 
    if i==5:
        continue
    print(i)
    i+=1
x = float(input('Insira o denominador: '))
"""
try:
    z = 1/x
    print(z)
except:
    print('Divisão por Zero detectada')


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