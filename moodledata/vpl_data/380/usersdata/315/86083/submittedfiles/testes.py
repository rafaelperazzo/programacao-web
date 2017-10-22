# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
from date time import datetime
from time import sleep

while true:
    hora = datetime.now()
    print(hora.strftime('%H:%M:%S'))
    sleep(1)



















"""""#EXERCICIO 14

soma=0
n = int(input('Digite um numero inteiro de 8 algarismos: '))
t = 100000000
if n>9999999 and n<1000000000:
 for i in range (0,9,1):
    soma = soma + (n//t)
    n=n%t
    t = t/10



else:
    print ('NAO SEI')
print (soma)


"""""































"""



visual = [['  ','  ','  '], ['  ','  ','  '], ['  ','  ','  ']]
for i in range(0,10,1):
    a = str(input('selecione a posção: '))
    if i%2==0:
        visual[int(a[0])][int(a[2])]='x'
    else:
        visual[int(a[0])][int(a[2])]='O'
    for i in range(0, 3, 1):
        print (str(visual[i][0]) + ' | ' + str(visual[i][1])  + ' | '+ str(visual[1][2]))




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
    