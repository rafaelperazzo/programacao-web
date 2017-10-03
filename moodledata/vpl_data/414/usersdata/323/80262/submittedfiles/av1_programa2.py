# -*- coding: utf-8 -*-
Mat=int(input('Digite sua matrícula: '))
Av1=float(input('Digite sua nota 1: '))
Av2=float(input('Digite sua nota 2: '))
Av3=float(input('Digite sua nota 3: '))
ME=float(input('Digite seu ME: '))
MA=(Av1+(Av2*2)+(Av3*3)+ME)/7
print (Mat)
print ('%.1f' %MA)
if MA>=9:
    print('A')
    print('APROVADO')
if MA>=7.5 and MA<9:
    print('B')
    print('APROVADO')
if MA>=6 and MA<7.5:
    print('C')
    print('APROVADO')
if MA>=4 and MA<6:
    print('D')
    print('REPROVADO')
if MA<4:
    print('E')
    print('REPROVADO')

   
    