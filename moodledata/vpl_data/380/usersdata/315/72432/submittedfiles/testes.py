# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import math

#CONSTANTES
g = 9.81
e = 0.000002

#ENTRADAS
f = float(input('digite f  '))
L = float(input('digite L  '))
Q = float(input('digite Q  '))
DH = float(input('digite DH  '))
v = float(input('digite v  '))

#FORMULA PARA D
x = (8*f*L*(Q**2))
y = ((math.pi**2)*g*DH)
D = (x/y)**(1/5)
print (x)
"""
#FORMULA PARA Rey
Rey = (4*Q)/(math.pi*D*v)

#FORMULA PARA K
z = e/3.7*D
p = 5.74/(Rey**0.9)
k = 0.25/(math.log10(z+p))**2

#SAIDAS
print ('%.4f' %D)
print ('%.4f' %Rey)
print ('%.4f' %k)
"""













"""
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
    