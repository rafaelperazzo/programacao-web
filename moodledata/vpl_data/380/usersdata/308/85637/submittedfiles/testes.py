# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input("Digite a quantidade de vezes: "))
for i in range (0, n+1, 1):
    print('Olá mundo')
"""
visual = [[' ',' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]
for i in range(0, 10, 1):
    a = str(input('Selecione a posição: '))
    if i%2==0:
        visual[int(a[0])][int(a[2])]='X'
    else: 
        visual[int(a[0])][int(a[2])]='O'
    for i in range (0, 3, 1):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))
        