# -*- coding: utf-8 -*-

matricula = input('Digite sua matrícula: ')
nota1 = float(input('Digite a nota da sua primeira avaliação: '))
nota2 = float(input('Digite a nota da sua segunda avaliação: '))
nota3 = float(input('Digite a nota da sua terceira avaliação: '))
ME = float(input('Digite a sua média de exercícios: '))

MA0 = float(((nota1) + (nota2 * 2) + (nota3 * 3) + (ME))/7)
MA = float('%.1f' % MA0)

print(matricula)
print(MA)

if MA >= 9:
    print('A')
    print('APROVADO')
if MA >= 7.5 and MA < 9:
    print('B')
    print('APROVADO')
if MA >= 6 and MA < 7.5:
    print('c')
    print('APROVADO')
if MA >= 4 and MA < 6:
    print('d')
    print('REPROVADO')
if MA < 4:
    print('E')
    print('REPROVADO')
