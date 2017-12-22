
from time import sleep
nome_do_jogador = input("Digite o seu nome: ") #Pede o nome do jogador
simb = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ") #o simbolo a ser usado

while(True):   #Verifica se o simbolo é vàlido
    if simb == "X" or simb == "O" :
        break
    else:
        simb = input("Digite um simbolo válido %s : " % nome_do_jogador)
coordenadas = [
            ('00', '01', '02')
            ,('10', '11','12')  #Matriz das coordenadas
            ,('20','21','22')
            ]

tabuleiro = [
            (' ', ' ', ' ')
            ,(' ', ' ', ' ')  #matriz tabuleiro
            ,(' ', ' ', ' ')
            ]
            
print(" ")
print(coordenadas[0][0]  + "|" + coordenadas[0][1] + ' ' + "|" + coordenadas[0][2]) 
print('---+--+---')
print(coordenadas[1][0]  + "|" + coordenadas[1][1] + ' ' + "|" + coordenadas[1][2])    #print coordenadas
print('---+--+---')
print(coordenadas[2][0]  + "|" + coordenadas[2][1] + ' ' + "|" + coordenadas[2][2])
sleep(1)
print(" ")
print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
print('---+--+---')
print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])    #print tabuleiro
print('---+--+---')
print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])

tabuleiro = []
for i in range (3):
    v = []
    for j in range(3):
        v.append(' ')
    tabuleiro.append(v)
    
    
        
n = input('Digite sua jogada: ')

i = int(n[0])
j = int(n[1])

tabuleiro[i][j] = simb

print(" ")
print(coordenadas[0][0]  + "|" + coordenadas[0][1] + ' ' + "|" + coordenadas[0][2]) 
print('---+--+---')
print(coordenadas[1][0]  + "|" + coordenadas[1][1] + ' ' + "|" + coordenadas[1][2])
print('---+--+---')
print(coordenadas[2][0]  + "|" + coordenadas[2][1] + ' ' + "|" + coordenadas[2][2])
sleep(0.7)
print(" ")
print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
print('---+--+---')
print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])
print('---+--+---')
print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])
print(' ')


