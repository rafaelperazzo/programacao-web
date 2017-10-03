# -*- coding: utf-8 -*-
matricula = input('Digite o numero da matricula :')
nota1 = float(input('Digite a primeira nota :'))
    print('nota1 :%.1f' %nota1')
nota2 = float(input('Digite a segunda nota :'))
nota3 = float(input('Digite a terceira nota :'))
ME = float(input('Digite a media dos exercicios :'))
MA = ((nota1 + (nota2*2) + (nota3*3) + ME))/7
print('Media de aproveitamento : %.1f' %MA)
if MA>=9 :
    print('Conceito A')
else:
    if MA>=7.5 and MA<9 :
        print('Conceito B')
    if MA>=6 and MA<7.5 :
        print('Conceito C')
    if MA>=4 and MA<6 :
        print('Conceito D')
    if MA<4 :
        print('Conceito E')

if (MA>=9) :
    print('Aprovado')
else: 
    if MA>=7.5 and MA<9 :
        print('Aprovado')
    if MA>=6 and MA<7.5 :
        print('Aprovado')
    if MA>=4 and MA<6 :
        print('Reprovado')
    if MA<4 :
        print('Reprovado')