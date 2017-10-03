# -*- coding: utf-8 -*-

Matricula = int(input('Digite o numero de matricula: '))
N1 = float(input('Digite o valor da N1: '))
N2 = float(input('Digite o valor da N2: '))
N3 = float(input('Digite o valor da N3: '))

ME = float(input('Digite a média dos exercícios: '))

MA = (N1 + (N2*2) + (N3*3) + ME)/(7)

if MA >= 9:
print(Conceito A)
elif 7.5 <= MA < 9:
print(Conceito B)
elif 6.5 <= MA < 7.5:
print(Conceito C)
elif 4 <= MA < 6.5:
print(Conceito D)
else:
    print(Conceito E)