# -*- coding: utf-8 -*-
matricula = int(input('digite a matricula: '))

nota1 = float(input('digite a nota1: '))
nota2 = float(input('digite a nota2: '))
nota3 = float(input('digite a nota3: '))
ME = float(input('digite a ME: '))

ma = (nota1 + (nota2 * 2) + (nota3 * 3) + ME)/7

if matricula != 0:
    print(matricula)
    
    print('%.f '%ma)