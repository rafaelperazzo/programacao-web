

nome_do_jogador = input("Digite o seu nome: ")
simb = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ")

while(True):
    if simb == "X" or simb == "O" :
        break
    else:
        simb = input("Digite um simbolo válido %s : " % nome_do_jogador)
coordenadas = [
            (00, 01, 02)
            ,(10, 11,12)
            ,(20,21,22)
            ]

tabuleiro = [
            (' ', ' ', ' ')
            ,(' ', ' ', ' ')
            ,(' ', ' ', ' ')
            ]
            
print(" ")
print(coordenadaso[0][0] + '  ' + "|" + coordenadaso[0][1] + ' ' + "|" + coordenadaso[0][2]) 
print('---+--+---')
print(coordenadaso[1][0] + '  ' + "|" + coordenadaso[1][1] + ' ' + "|" + coordenadaso[1][2])
print('---+--+---')
print(coordenadaso[2][0] + '  ' + "|" + coordenadaso[2][1] + ' ' + "|" + coordenadaso[2][2])

print(" ")
print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
print('---+--+---')
print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])
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
print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
print('---+--+---')
print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])
print('---+--+---')
print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])

