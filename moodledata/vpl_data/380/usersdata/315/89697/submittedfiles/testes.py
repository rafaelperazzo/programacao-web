# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random
import time


x = random.choice(('a','b'))
print (x)

























"""
def imprimeCampo(campo):
        c = 0
        
        for i in campo:
                if c % 3 == 0:
                        print ("")
                        c = 0
                print (i),
                c += 1
                
        print ("\n")

def ganhou(simbolo, campo):
        if campo[0] == simbolo and campo[1] == simbolo and campo[2] == simbolo:
                return 1

        if campo[3] == simbolo and campo[4] == simbolo and campo[5] == simbolo:
                return 1

        if campo[6] == simbolo and campo[7] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[3] == simbolo and campo[6] == simbolo:
                return 1

        if campo[1] == simbolo and campo[4] == simbolo and campo[7] == simbolo:
                return 1
        
        if campo[2] == simbolo and campo[5] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[4] == simbolo and campo[8] == simbolo:
                return 1

        if campo[2] == simbolo and campo[4] == simbolo and campo[6] == simbolo:
                return 1

def velha(campo):
        if '_' not in campo:
                return 1
        

import random

campo = ['_','_','_','_','_','_','_','_','_']

jogador = random.choice((0,1))

if jogador == 1:
        sVC = 'X'
        sPC = 'O'
else:
        sPC = 'X'
        sVC = 'O'

print ("Voce e' %s" % sVC)
print ("O Pc e' %s" % sPC)

while 1:
        if velha(campo):
                imprimeCampo(campo)
                print ("VELHA")
                break
        if jogador:
                imprimeCampo(campo)
                
                while 1:
                        vc = int(input())

                        if campo[vc] == '_':
                                break

                campo[vc] = sVC

                jogador = 0

                if ganhou(sVC,campo):
                        imprimeCampo(campo)
                        print ("VC GANHOU")
                        break

        else:
                imprimeCampo(campo)
                while 1:
                        pc = random.randint(0,8)

                        if campo[pc] == '_':
                                break

                campo[pc] = sPC

                jogador = 1
        
                if ganhou(sPC,campo):
                        imprimeCampo(campo)
                        print ("PC GANHOU")
                        break




"""









































"""

visual = [['  ','  ','  '], ['  ','  ','  '], ['  ','  ','  ']]
for i in range(0,9,1):
    a = str(input('selecione a posção: '))
    if i%2==0:
        visual[int(a[0])][int(a[2])]='x'
    else:
        visual[int(a[0])][int(a[2])]='O'
    for i in range(0, 3, 1):
        print ( str(visual[i][0]) + ' | ' + str(visual[i][1])  + ' | '+ str(visual[i][2] ))



"""










"""

# Média de Provas
aprovados = []
reprovados = []
final = []


quant_alunos = int(input('Digite a quantidade de alunos da turma: '))

def avaliaSituacaoAluno():
    media = (nota1+nota2+nota3+nota4) / 4.0
    if media >= 7:
        aprovados.append(nome)
        print (nome, media, "- Aprovado")
    else:
        nota_minima_final = (50 - (media * 6)) / 4.0
        if nota_minima_final > 10:
            reprovados.append(nome)
            print (nome, media, "- Reprovado")
        else:
            final.append(nome)
            print (nome, media, "- Final")
        
def imprimeSaida():
    print ('\n Aprovados:')
    for aluno in aprovados:
       print (aluno),
    print ('\n Reprovados:')
    for aluno in reprovados:
           print (aluno),
    print ('\n Final:')
    for aluno in final:
        print (aluno),


for iteracao in range(quant_alunos):
    nome = input('\nNome aluno: ')
    nota1 = float(input('Nota prova1: '))
    nota2 = float(input('Nota prova2: '))
    nota3 = float(input('Nota prova3: '))
    nota4 = float(input('Nota prova4: '))
    avaliaSituacaoAluno()
    
imprimeSaida()
    
""" 
    