# -*- coding: utf-8 -*-
matricula = str(input('Numero de matricula: '))
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
ME = float(input('Insira a media dos exercicios: '))

MA = (nota1 + (nota2*2) + (nota3*3) + ME)/7

print (matricula)
print ('%.1f' % MA)

if MA>=9:
    print ('A')
if MA<9 and MA>=7.5:
    print ('B')
if MA<7 and MA>=6:
    print ('C')
if MA<6 and MA>=4:
    print ('D')
if MA<4:
    print ('E')

if MA>=6:
    print ('APROVADO')
if MA<6:
    print ('REPROVADO')