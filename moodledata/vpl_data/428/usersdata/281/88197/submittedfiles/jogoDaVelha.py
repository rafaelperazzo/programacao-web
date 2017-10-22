# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import *

# COLOQUE SEU PROGRAMA A PARTIR DAQUI
'''
print('Bem vindo ao jogo da velha da equipe ...')
nome=str(input('Qual o seu nome (ou apelido)? '))
simb ()
import random
print(random.choice(1,2))
'''
import random


    campo = ['_','_','_','_','_','_','_','_','_']

    jogador = random.choice((0,1))

    if jogador == 1:
            sVC = 'X'
            sPC = 'O'

    else:
            sPC = 'X'
            sVC = 'O'

    print ("Voce e' %s" % sVC)
    print ("O Pc e' %s" % sPC)

    while 1:
            if velha(campo):
                    imprimeCampo(campo)
                    print ("VELHA")
                    break
            if jogador:
                    imprimeCampo(campo)

                    while 1:
                            vc = int(input())

                            if campo[vc] == '_':
                                    break

                    campo[vc] = sVC

                    jogador = 0

                    if ganhou(sVC,campo):
                            imprimeCampo(campo)
                            print ("VC GANHOU")
                            break

            else:
                    imprimeCampo(campo)
                    while 1:
                            pc = random.randint(0,8)

                            if campo[pc] == '_':
                                    break

                    campo[pc] = sPC

                    jogador = 1

                    if ganhou(sPC,campo):
                            imprimeCampo(campo)
                            print ("PC GANHOU")
                            break

    
        
        
   
