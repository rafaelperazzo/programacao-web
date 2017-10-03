# -*- coding: utf-8 -*-
matricula = input('Digite a matricula: ')
nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
nota3 = float(input('Digite a nota3: '))
ME = float(input('Digite a media dos exercicios: '))
MA = (nota1 + (nota2*2) + (nota3*3) + ME)/7
print (matricula)
print ('%.1f' %MA)
x = ('REPROVADO')
y = ('APROVADO')
if MA >= 9:
    print ('A')
elif 7.5 <= MA < 9:
    print ('B')
elif 6 <= MA < 7.5:
    print ('C')
elif 4 <= MA < 6:
    print ('D')
elif MA < 4:
    print ('E')
if 'D' or 'E':
print (x)
else:
    if 'A' or 'B' or 'C':
    print (y)