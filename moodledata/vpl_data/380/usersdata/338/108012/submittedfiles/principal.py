

nome_do_jogador = input("Digite o seu nome: ")
simb = input("Digite o simbolo com o qual vocÊ quer jogar [X ou O] : ")

while(True):
    if simb == "X" or simb == "O" :
        break
    else:
        simb = input("Digite um simbolo válido %s : " % nome_do_jogador)

tabuleiro = [
            (' ', ' ', ' ')
            ,(' ', ' ', ' ')
            ,(' ', ' ', ' ')
            ]
            
print(" ")
print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
print('---+--+---')
print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])
print('---+--+---')
print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])


n = input('Digite sua jogada: ')
print(n[0])

i = int(n[0])
j = int(n[1])

if i == 0 :
    tabuleiro[j] = simb
    print(" ")
    print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
    print('---+--+---')
    print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])
    print('---+--+---')
    print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])

if i == 1 :
    tabuleiro[j] = simb
    

if i == 2 :
    tabuleiro[j] = simb
    
print("nada")

#jogo_d_v[int(n[0])] [int(n[1])] = "X"

#print(jogo_d_v[0][0] + "|" + jogo_d_v[0][1] + "|" + jogo_d_v[0][1]) 
#print(jogo_d_v[1][0] + "|" + jogo_d_v[1][1] + "|" + jogo_d_v[1][2])
#print(jogo_d_v[2][0] + "|" + jogo_d_v[2][1] + "|" + jogo_d_v[2][2])
