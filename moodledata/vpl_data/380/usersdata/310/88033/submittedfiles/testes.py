# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO

def imprimeCampo(campo):
        c = 0
        
        for i in campo:
                if c % 3 == 0:
                        print ("")
                        c = 0
                print (i),
                c += 1
                
        print ("\n")

def ganhou(simbolo, campo):
        if campo[0] == simbolo and campo[1] == simbolo and campo[2] == simbolo:
                return 1

        if campo[3] == simbolo and campo[4] == simbolo and campo[5] == simbolo:
                return 1

        if campo[6] == simbolo and campo[7] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[3] == simbolo and campo[6] == simbolo:
                return 1

        if campo[1] == simbolo and campo[4] == simbolo and campo[7] == simbolo:
                return 1
        
        if campo[2] == simbolo and campo[5] == simbolo and campo[8] == simbolo:
                return 1

        if campo[0] == simbolo and campo[4] == simbolo and campo[8] == simbolo:
                return 1

        if campo[2] == simbolo and campo[4] == simbolo and campo[6] == simbolo:
                return 1

def velha(campo):
        if '_' not in campo:
                return 1
        

import random

campo = [['_','_','_'],['_','_','_'],['_','_','_']]

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
                        vc = int(input('diga sua jogada: '))

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


























"""
import random
k = 0
while k==0:
# 
#
#
#
#
    print('Bem vindo ao JogoDaVelha do Grupo 1 [Caio,Hugo,Anderson,Juan]') 
    a = input('Digite seu nome:')
    b = input('Digite qual simbolo você quer usar, X ou O :  ')
    while b!= 'X' and b!= 'O' and b!= 'x' and b!= 'o':
        b = input('Digite qual simbolo você quer usar, X ou O :  ')
    
    começo =random.randint(0,1)
    print (começo)
    if começo==0:
        print('Computador começa')
    else:
        print('Jogador começa')








    k = int(input('\n\nSe quiser jogar denovo digite 0:'))
    print ('\n\n\n')
    
    
"""