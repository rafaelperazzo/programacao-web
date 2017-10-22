# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

b = 0
a=1
for i in range (0,a,1):
    if a%(i+1)!=0:
        b=b+1



















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
    