

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
print(tabuleiro3[0] + '  ' + "|" + tabuleiro3[1] + ' ' + "|" + tabuleiro3[2])

lista = []
n = input('Digite sua jogada: ')
lista.append(n)
print(n[0])

i = int(n[0])
j = int(n[1])

if i == 0 :
    tabuleiro1[j] = simb
    print(tabuleiro1[0] + '  ' + "|" + tabuleiro1[1] + ' ' + "|" + tabuleiro1[2]) 
    print('---+--+---')
    print(tabuleiro2[0] + '  ' + "|" + tabuleiro2[1] + ' ' + "|" + tabuleiro2[2])
    print('---+--+---')
    print(tabuleiro3[0] + '  ' + "|" + tabuleiro3[1] + ' ' + "|" + tabuleiro3[2])

if i == 1 :
    tabuleiro2[j] = simb
    

if i == 2 :
    tabuleiro3[j] = simb
    
print("nada")

#jogo_d_v[int(n[0])] [int(n[1])] = "X"

#print(jogo_d_v[0][0] + "|" + jogo_d_v[0][1] + "|" + jogo_d_v[0][1]) 
#print(jogo_d_v[1][0] + "|" + jogo_d_v[1][1] + "|" + jogo_d_v[1][2])
#print(jogo_d_v[2][0] + "|" + jogo_d_v[2][1] + "|" + jogo_d_v[2][2])
