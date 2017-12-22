# -*- coding: utf-8 -*-
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
