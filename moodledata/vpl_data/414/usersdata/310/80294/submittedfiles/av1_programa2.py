# -*- coding: utf-8 -*-

Matricula = int(input('Digite o numero de matricula: '))
N1 = float(input('Digite o valor da N1: '))
N2 = float(input('Digite o valor da N2: '))
N3 = float(input('Digite o valor da N3: '))

ME = float(input('Digite a média dos exercícios: '))

MA = (N1 + (N2*2) + (N3*3) + ME)/(7)

print(Matricula)
print(MA)

if MA >= 9:
    print('A')
elif 7.5 <= MA < 9:
    print('B')
elif 6.5 <= MA < 7.5:
    print('C')
elif 4 <= MA < 6.5:
    print('D')
else:
    print('E')
if MA >= 6:
    print('APROVADO')
else:
    print('REPROVADO')