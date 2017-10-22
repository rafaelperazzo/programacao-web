# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

n = int(input('Digite a senha: '))
while n<0 and n>9999:
    if n==1234:
        print ('Parabéns!!!  Você acertou')
    else:
        print ('senha Inválida!!!\n tente novamente')
        n = int(input('Digite a senha: '))




















"""
a = float(input('a'))
b = float(input('b'))
c = float(input('c'))
d = float(input('d'))


if a>b and a>c and a>d:
    print('a é maior')
elif b>a  and b>c and b>d:
    print ('b e maior')
elif c>a and c>b and c>d:
    print ('c é maior')
elif a==b==c==d:
    print ('sao iguais')
else:
    print('d é maior')
    
    
if a<b and a<c and a<d:
    print('a é menor')
elif b<a  and b<c and b<d:
    print ('b e menor')
elif c<a and c<b and c<d:
    print ('c é menor')
elif a==b==c==d:
    print('sao iguais')
    
else:
    print ('d e menorr')


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
    