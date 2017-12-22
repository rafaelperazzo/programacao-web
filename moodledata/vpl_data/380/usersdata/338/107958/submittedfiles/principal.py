
nome_do_jogador = input("Digite o seu nome: ")
simb = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ")

while(True):
    if simb == "X" or simb == "O" :
        break
    else:
        simb = input("Digite um simbolo válido %s : " % nome_do_jogador)

tabuleiro1 = (' ', ' ', ' ')
tabuleiro2 = (' ', ' ', ' ')
tabuleiro3 = (' ', ' ', ' ')
            
print(" ")
print(tabuleiro1[0] + '  ' + "|" + tabuleiro1[1] + ' ' + "|" + tabuleiro1[2]) 
print('---+--+---')
print(tabuleiro2[0] + '  ' + "|" + tabuleiro2[1] + ' ' + "|" + tabuleiro2[2])
print('---+--+---')
print(tabuleiro3[0] + '  ' + "|" + tabuleiro3[1] + ' ' + "|" + tabuleiro3[2]
"""
n = input('Digite sua jogada: ')
if n[0] == 0:
    tabuleiro1[n[1]] = simb
    
if n[0] == 1:
    tabuleiro2[n[1]] = simb
    
if n[0] == 2:
    tabuleiro3[n[1]] = simb


jogo_d_v[int(n[0])] [int(n[1])] = "X"

print(jogo_d_v[0][0] + "|" + jogo_d_v[0][1] + "|" + jogo_d_v[0][1]) 
print(jogo_d_v[1][0] + "|" + jogo_d_v[1][1] + "|" + jogo_d_v[1][2])
print(jogo_d_v[2][0] + "|" + jogo_d_v[2][1] + "|" + jogo_d_v[2][2])


n = input('digite sua jogada: ')
if n[0] == 0:
    
if n[0] == 1:
    
if n[0] == 2:
n[2] = lista
"""