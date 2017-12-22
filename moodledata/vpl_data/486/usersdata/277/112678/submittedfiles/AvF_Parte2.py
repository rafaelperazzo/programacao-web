# -*- coding: utf-8 -*-
"""
TEMPO ESTIMADO: 12h15
"""
idades=[]
alturas=[]
# lendo os dados da pesquisa
while True:
    idade = int(input('Digite a idade: '))
    if (idade == -1):
        break
    if (idade < 18):
        continue
    idades.append(idade)
    while True:
        altura = float(input('Digite a altura: '))
        if (altura > 0.0):
            break
    alturas.append(altura)
# processando
cont_alunos = 0
media = sum(alturas)/float(len(alturas))
for i in range(len(idades)):
    if (idades[i] > 25):
        if (alturas[i] < media):
            cont_alunos+=1
print(cont_alunos)