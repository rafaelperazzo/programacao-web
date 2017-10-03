# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
nome = input('\nNome aluno: ')
Nota1 = input('Nota prova1: ')
Nota2 = input('Nota prova2: ')
Nota3 = input('Nota prova3: ')
Nota4 = input('Nota prova4: ')

media = (10+9+7+7) / 4.0
if media >= 7:
    print (nome, media, "- Aprovado")
else:
    nota_minima_final = (50 - (media * 6)) / 4.0
    if nota_minima_final > 10:
        print (nome, media, "- Reprovados")
    else:
        print (nome, media, "- Final")