# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
print('Seja bem vindo ao programa exemplo!')
print('---------------------------------------------------\n')
nome = str(input('Qual o seu nome?'))
print('Olá '+nome+'. Farei algumas perguntas sobre você.')
idade = int(input(′Qual a sua idade?′))
print('Ok. Voce tem %d anos.' % idade)
altura = float(input(′Qual a sua altura em metros?'))
print('Voce tem %.2f de altura.' % altura)
estudante = bool(input(′Você eh estudante? (Sim: True; Não: False)'))
print('\n\nIsso é tudo. Até a próxima, %s!' % nome)
print('---------------------------------------------------')