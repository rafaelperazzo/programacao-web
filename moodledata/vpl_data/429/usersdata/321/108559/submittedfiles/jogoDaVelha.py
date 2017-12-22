# # -*- coding: utf-8 -*-
# from jogoDaVelha_BIB import *

# # COLOQUE SEU PROGRAMA A PARTIR DAQUI
# print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

# a=nome()

# b=solicitaSimboloDoHumano()

# sort=sorteioPrimeiraJogada(a)

# if sort==0:
#     if b == 'X':
#         c = ' O '
#     else:
#         c = ' X '
#     JogadaComputador(c)
#     mostrarTabuleiro()
#     p=JogadaHumana(a,b)
# else:
#     if b == 'X':
#         c = ' O '
#     else:
#         c = ' X '
#     p=JogadaHumana(a,b)
#     JogadaComputador(c)
#     mostrarTabuleiro()
            
# while not verificaVencedor(b,tabuleiro,a):
#     if sort==0:
#         if JogadaComputador(c):
#             mostrarTabuleiro()
#             JogadaHumana(a,b)
              
#     else:
#         if JogadaHumana(a,b):
#             JogadaComputador(c)
#             mostrarTabuleiro()
            
            

#     #if not jogueNovamente():
#         #break
                
#---------------------------------------------------------
# por Iara
#---------------------------------------------------------

# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

print('Bem vindo ao JogoDaVelha do grupo 8 [Iara, Ingrid, Luiz Otávio, Tatiane]\n')

#solicitar o nome da pessoa ou o apelido
nome = input('\nQual seu nome (ou apelido)? ')

#solicitar o símbolo da pessoa
simboloIndex = solicitaSimboloDoHumano()

#sortear a primeira jogada
primeiro = sorteioPrimeiraJogada(nome)

#primeiro == 0 é computador
def proximaJogada(primeiro):
    #mostar tela
    mostrar = False
    #joagada
    if primeiro == 0:
        jogadaComputador(simboloIndex)
        mostrar = True
    else:
        jogadaHumana(nome, simboloIndex)
    #mostrar a tela?
    if mostrar:
        mostraTabuleiro()
    #verificar vencedor
    if verificaVencedor(nome, simboloIndex):
        return
    proximaJogada(not primeiro)

proximaJogada(primeiro)