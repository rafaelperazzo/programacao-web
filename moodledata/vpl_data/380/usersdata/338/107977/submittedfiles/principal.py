
n = input(' Digiti: ')
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
"""            
print(" ")
print(tabuleiro1[0] + '  ' + "|" + tabuleiro1[1] + ' ' + "|" + tabuleiro1[2]) 
print('---+--+---')
print(tabuleiro2[0] + '  ' + "|" + tabuleiro2[1] + ' ' + "|" + tabuleiro2[2])
print('---+--+---')
print(tabuleiro3[0] + '  ' + "|" + tabuleiro3[1] + ' ' + "|" + tabuleiro3[2]
"""