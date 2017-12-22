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
fim = True
while True:
    #jogada do computador e do humano
    jogadaHumana(nome, simboloIndex)
    if verificaVencedor(nome, simboloIndex):
        print('Vencedor: %s % nome)
    jogadaComputador(simboloIndex)
    mostraTabuleiro()
    if verificaVencedor(nome, simboloIndex):
        print('Vencedor: %s' % nome)
