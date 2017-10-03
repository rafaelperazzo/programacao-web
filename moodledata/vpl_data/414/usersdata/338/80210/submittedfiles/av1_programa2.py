# -*- coding: utf-8 -*-

matricula = input('Digite sua matrícula: ')
nota1 = float(input('Digite a nota da sua primeira avaliação: '))
nota2 = float(input('Digite a nota da sua segunda avaliação: '))
nota3 = float(input('Digite a nota da sua terceira avaliação: '))
ME = float(input('Digite a sua média de exercícios: '))

MA = ((nota1) + (nota2 * 2) + (nota3 * 3) + (ME))/7
print(MA)
"""
print(nota1)
print(nota2)
print(nota3)
print(ME)
"""