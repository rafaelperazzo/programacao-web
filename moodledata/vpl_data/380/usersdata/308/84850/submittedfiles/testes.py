# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
visual = [['','', ''], ['', '',''], ['', '', '']]

a = int(input('Selecione a posição: '))
visual[int(a[0])][int(a[2])]='X'
for i in range (0, 3, 1):
    print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))
012
1 0