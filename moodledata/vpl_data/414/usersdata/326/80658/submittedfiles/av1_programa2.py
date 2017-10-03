# -*- coding: utf-8 -*-
matricula = int(input('digite a matricula: '))

nota1 = float(input('digite a nota1: '))
nota2 = float(input('digite a nota2: '))
nota3 = float(input('digite a nota3: '))
ME = float(input('digite a ME: '))

ma = (nota1 + (nota2 * 2) + (nota3 * 3) + ME)/7

    
if ma >=9:
    print(matricula)
    print('%.1f '%ma)
    print('A')
if 7.5 <= ma < 9:
    print(matricula)
    print('%.1f '%ma)
    print('B')
if 6 <= ma < 7.5:
    print(matricula)
    print('%.1f '%ma)
    print('C')
if 4 <= ma < 6:
    print(matricula)
    print('%.1f '%ma)
    print('D')
if ma < 4:
    print(matricula)
    print('%.1f '%ma)
    print('E')
if ma >= 6:
    print('APROVADO')
    elif:
        print('REPROVADO')
    
    