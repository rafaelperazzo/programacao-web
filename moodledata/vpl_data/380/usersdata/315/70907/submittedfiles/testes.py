# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
nome = input('\nNome aluno: ')
a = input('Nota prova1: ')
b = input('Nota prova2: ')
c = input('Nota prova3: ')
d = input('Nota prova4: ')

media = (a+b+c+d) / 4.0
if media >= 7:
    print (nome, media, "- Aprovado")
else:
    nota_minima_final = (50 - (media * 6)) / 4.0
    if nota_minima_final > 10:
        print (nome, media, "- Reprovados")
    else:
        print (nome, media, "- Final")