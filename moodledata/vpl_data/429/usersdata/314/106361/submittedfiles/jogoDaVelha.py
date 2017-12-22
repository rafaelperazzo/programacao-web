'''Sua biblioteca de funções deverá implementar, obrigatoriamente, as seguintes funções:

solicitaSimboloDoHumano: solicita ao usuário o símbolo que ele deseja utilizar na partida e garante que ele informou um símbolo válido (X ou O);
sorteioPrimeiraJogada: realiza um sorteio totalmente aleatório para definir quem começa o jogo (humano ou computador);
jogadaHumana: recebe uma jogada válida do usuário;
jogadaComputador: realiza uma jogada válida pelo computador;
validaJogada: verifica se o jogador inseriu ou realizou uma jogada válida;
mostraTabuleiro: exibe o tabuleiro atualizado na tela.
verificaVencedor: verifica se há vencedor ou empate e, caso positivo, exibe “Vencedor: Computador” (sem as aspas) ou “Vencedor:
nome” (nome é o valor do nome ou apelido do jogador humano informado no começo, sem as aspas) ou “Deu Velha!” (empate!, sem as aspas).
'''

from JogoDaVelha_BIB import *

tabuleiro = [ [' ',' ',' '], [' ',' ',' '], [' ',' ',' '] ] #Tabuleiro vazio

grupo = 'H [Breendon, Gustavo, Roberto, Rafael]' #Nome dos integrantes do grupo
jogador = ['','']                                #Nome do jogador e simbolo
computador = ['Computador','']                   #Computador e simbolo



bemVindo(grupo)

jogador[0] = input('Qual o seu nome (ou apelido)? ')
jogador[1], computador[1] = solicitaSimboloDoHumano()

turno = sorteioPrimeiraJogada(jogador[0])
movimentos = 0
print('Vencedor do sorteio para início do jogo: {}' .format(turno))

acabou = False
while not acabou :
    if turno == computador[0] :
        tabuleiro = jogadaComputador(tabuleiro, computador[1])
        mostraTabuleiro(tabuleiro)
        movimentos += 1
        acabou = verificaVencedor(tabuleiro, computador, movimentos)
        turno = jogador[0]
    else :
        while True :
            jogada = input('Qual a sua jogada, {}? ' .format(jogador[0]))
            jogadaValida = validaJogada(tabuleiro, jogada)
            if not jogadaValida :
                print('OPS!!! Essa jogada não está disponível. Tente novamente!')
            else :
                tabuleiro = jogadaHumana(tabuleiro, jogador[1], jogada)
                movimentos += 1
                acabou = verificaVencedor(tabuleiro, jogador, movimentos)
                turno = computador[0]
                break




'''
Bem vindo ao JogoDaVelha do grupo X [ A, B, C e D ]

Qual o seu nome (ou apelido)?  Max

Qual símbolo você deseja utilizar no jogo?  X

Vencedor do sorteio para início do jogo: Computador

 O  |     |

      |     |

      |     |

Qual a sua jogada, Max?  1 1

  O  |      |  O

      |  X  |

      |      |

 Qual a sua jogada, Max?  0 1

  O  |  X  |  O

      |  X  |

      |  O  |

Qual a sua jogada, Max?  2 1

OPS!!! Essa jogada não está disponível. Tente novamente!

Qual a sua jogada, Max?  1 0

 O  |  X  |  O

 X   |  X  |

 O   |  O  |

Qual a sua jogada, Max? 1 2

 O  |  X  |  O

 X   |  X  |  X

 O   |  O  |

Vencedor: Max'''
