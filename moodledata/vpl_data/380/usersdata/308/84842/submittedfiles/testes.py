# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
visual = [['','', ''], ['', '',''], ['', '', '']]

a = int(input('Selecione a linha: '))
b = int(input('Selecione a coluna: '))
visual[a][b]='X'
for i in range (0, 3, 1):
    print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))

