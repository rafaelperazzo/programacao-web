import random

simbolos = ['X', 'O']             # Símbolos utilizados pelos jogadores
valoresValidos = ['0','1','2']    # Posições válidas de linha ou coluna no tabuleiro
velha = 9                         # Após 9 movimentos sem vencedor, deu velha (empate)

# Mensagem de Boas-Vindas
def bemVindo(nomeGrupo):
    print('Bem vindo ao JogoDaVelha do grupo {}\n' .format(nomeGrupo))

# Solicita do jogador qual símbolo ele deseja utilizar na partida, retornando uma lista
# contendo o simbolo do jogador e o simbolo do segundo jogador, respectivamente.
def solicitaSimboloDoHumano() :

    while True :
        simbolo = input('\nQual símbolo você deseja utilizar no jogo? \n').upper().strip()
        if simbolo not in simbolos :
            print('Símbolo inválido. Escolha {} ou {}.' .format(simbolos[0], simbolos[1]))
        else: break

    if simbolo == simbolos[0]:
        return ['X', 'O']
    else:
        return ['O', 'X']


# Sorteia quem iniciará a partida
def sorteioPrimeiraJogada(nomeJogador) :
    return random.choice([nomeJogador, 'Computador'])

def jogadaHumana(tabuleiro, simbolo, jogada) :
    aux = jogada.split()
    tabuleiro[int(aux[0])][int(aux[1])] = simbolo
    return tabuleiro

# Jogada do computador (posição vazia aleatória)
def jogadaComputador(tabuleiro, simbolo):

    while True:
        jogada = [random.choice([0, 1, 2]), random.choice([0, 1, 2])]
        if tabuleiro[jogada[0]][jogada[1]] == ' ' :
            tabuleiro[jogada[0]][jogada[1]] = simbolo
            break
    return tabuleiro

def validaJogada(tabuleiro, jogada) :
    aux = jogada.split()
    if len(aux) != 2 :
        return False
    elif (aux[0] not in valoresValidos) or (aux[1] not in valoresValidos) :
        return False
    else:
        if tabuleiro[int(aux[0])][int(aux[1])] == ' ' :
            return True
        else:
            return False

# Verifica se houve vencedor ou o jogo terminou empataddo
def verificaVencedor(tabuleiro, jogador, jogadas) :

    if (jogador[1] == tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2]) or (jogador[1] == tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2]) or (jogador[1] == tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2]) or (jogador[1] == tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0]) or (jogador[1] == tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1]) or (jogador[1] == tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2]) or (jogador[1] == tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]) or (jogador[1] == tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0]) :
        if jogador[0]!= 'Computador':
            mostraTabuleiro(tabuleiro)
        print('Vencedor: {}' .format(jogador[0]))
        return True
    elif jogadas == velha :
        print('Deu Velha!')
        return True
    else :
        return False

# Imprime o tabuleiro na tela, com cada posição separado por uma barra ('|')
def mostraTabuleiro(tabuleiro) :
    print(tabuleiro[0][0] + ' | ' + tabuleiro[0][1] + ' | ' + tabuleiro[0][2])
    print(tabuleiro[1][0] + ' | ' + tabuleiro[1][1] + ' | ' + tabuleiro[1][2])
    print(tabuleiro[2][0] + ' | ' + tabuleiro[2][1] + ' | ' + tabuleiro[2][2])
