# -*- coding: utf-8 -*-
matricula = input('Digite a matricula: ')
nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
nota3 = float(input('Digite a nota3: '))
ME = float(input('Digite a media dos exercicios: '))
MA = (nota1 + (nota2*2) + (nota3*3) + ME)/7
print (matricula)
print ('%.1f' %MA)
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
    
if (MA = 'D' or 'E'):
    print ('REPROVADO')
else:
    if (MA = 'A' or 'B' or 'C'):
        print ('APROVADO')