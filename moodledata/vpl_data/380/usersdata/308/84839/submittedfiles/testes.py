# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
visual = [['','', ''], ['', '',''], ['', '', '']]

a = int(input('Selecione a linha: '))
b = int(input('Selecione a coluna: '))
visual[a][b]='X'
for i in range (0, 3, 1):
    print(str(b[i][0]) + ' | '+ str(b[i][1])  + ' | '+ str(b[i][2]))

