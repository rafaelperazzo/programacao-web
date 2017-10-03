# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
nome = input('\nNome aluno: ')
nota1 = float(input('Nota prova1: '))
nota2 = float(input('Nota prova2: '))
nota3 = float(input('Nota prova3: '))
nota4 = float(input('Nota prova4: '))

media = (nota1+nota2+nota3+nota4) / 4.0
if media >= 7:
    print (nome, media, "- Aprovado")
else:
    nota_minima_final = (50 - (media * 6)) / 4.0
    if nota_minima_final > 10:
        print (nome, media, "- Reprovados")
    else:
        print (nome, media, "- Final")