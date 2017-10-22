# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = 0
for j in range (10, 100, 1):
    n=n+1
    
if 1==2:
    visual = [[' ',' ', ' '], [' ', ' ',' '], [' ', ' ', ' ']]  
    #for i in range(0, 10, 1):
    a = str(input('Selecione a posição: '))
    if i%2==0:
        visual[int(a[0])][int(a[2])]='X'
    else: 
        visual[int(a[0])][int(a[2])]='O'
    for i in range (0, 3, 1):
        print(str(visual[i][0]) + ' | '+ str(visual[i][1])  + ' | '+ str(visual[i][2]))