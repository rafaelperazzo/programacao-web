# -*- coding: utf-8 -*-
from minha_bib import *

#COMECE AQUI ABAIXO

matriz = [
    ['   ','   ','   '],
    ['   ','   ','   '],
    ['   ','   ','   ']
    ]

print (matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])

while 1:
    n = input('digite')
    print (n)
    print(n[0])
    print(n[2])
    
    matriz[int(n[0])][int(n[2])] = ' X '
    
    print (matriz[0][0] + '|' + matriz[0][1] + '|' + matriz[0][2])
    print (matriz[1][0] + '|' + matriz[1][1] + '|' + matriz[1][2])
    print (matriz[2][0] + '|' + matriz[2][1] + '|' + matriz[2][2])
    print (matriz)
    if matriz == [[' X ',' X ',' X '], [' X ',' X ',' X '], [' X ',' X ',' X ']]:
        break











a1 = ' '
a2 = ' '
a3 = ' '
a4 = ' '
a5 = ' '
a6 = ' '
a7 = ' '
a8 = ' '
a9 = ' '

print(' '+ a1 + ' |' + ' '+a2 + ' |' + ' '+a3 +'\n---+---+---' + '\n '+ ''+a4 + ' |' + ' '+a5 + ' |' + ' '+a6 +'\n---+---+---' + '\n '+ ''+a7 + ' |' + ' '+a8 + ' |' + ' '+a9 )

#00=a1 #01=a2 #02=a3
#10=a4 #11=a5 #12=a6
#20=a7 #21=a8 #22=a9






"""
print('Bem vindo ao jogo da velha')
nome = input('Qual seu nome: ')
jogador = 0
smbH = 'b'
solicitaSimbolodoHumano(smbH)
sorteioPrimeiraJogada(jogador)
jogadaComputador(a)

while True:
    if jogador ==1:
        while True:
            jogadaHumana(a)
    
    
    else:
        JogadaComputador(pc)

"""