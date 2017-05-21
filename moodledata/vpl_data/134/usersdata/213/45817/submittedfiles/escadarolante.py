# -*- coding: utf-8 -*-
numeroPessoas=int(input('Informe o número de pessoas que entraram na fila: '))
tempoInicial=int(input('Informe o primeiro tempo: '))
contador=10
for i in range(2,n+1,1):
    tempo=int(input('Informe o tempo que a pessoa entrou: '))
    x=tempo-tempoInicial
    contador=contador+x
    tempoInicial=tempo
print(contador)