# -*- coding: utf-8 -*-
matricula=input('Digite o número da matrícula aqui:')
nota1=float(input('nota 1 com uma casa decimal:'))
nota2=float(input('nota 2 com uma casa decimal:'))
nota3=float(input('nota 3 com uma casa decimal:'))
ME=float(input('média dos exercicios com uma casa decimal:'))
print(matricula)
MA=((nota1+(nota2*2)+(nota3*3)+ME)/7)
print('%.1f'%MA)
if (MA>=9):
    print('A')
if (7.5<=MA<9):
    print('B')
if (6<=MA<7.5):
    print('C')
if (4<=MA<6):
    print('D')
if (MA<4):
    print('E'):
        
   
    