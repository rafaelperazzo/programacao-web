# -*- coding: utf-8 -*-

aprovados = []
reprovados = []

n = int(input('competidores: '))
p = float(input('nota minima: '))

def avaliarcompetidores():
    if T[i]+J[i] >= p:
        aprovados.append(T[i]+J[i])
    else:
        reprovados.append(T[i]+J[i])
        
def imprimesaida():
    print('\nAprovados:')
    for alunos in aprovados:
        print(aprovados),
    print('\nReprovados:')
    for alunos in reprovados:
        print(reprovados),


T = [0]*n
J = [0]*n

for i in range (n):
    T[i] = int(input('Nota 1: '))
    J[i] = int(input('Nota 2: '))
    avaliarcompetidores()












