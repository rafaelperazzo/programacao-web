# -*- coding: utf-8 -*-
from jogoDaVelha_BIB import verificar_vitoria
from jogoDaVelha_BIB import sorteio
from jogoDaVelha_BIB import sorteio2
import time
from jogoDaVelha_BIB import jogadauser
from jogoDaVelha_BIB import jogadapc
# COLOQUE SEU PROGRAMA A PARTIR DAQUI
tabuleiro=[[1,2,3],[1,2,3],[1,2,3]]
for i in range(0,3,1):
    for j in range(0,3,1):
        tabuleiro[i][j]=" "

print('---------------------------------------')
print('JOGO DA VELHA')
print('Olá\nSeja Bem Vindo ao jogo da velha!')


nome1=str(input('Qual seu nome(ou apelido)? '))

s1=str(input('Qual símbolo você deseja utilizar,'+nome1+'?[X/O]'))
if s1=='X':
    s2='O'
else:
    s2='X'
print('Esse é o nosso tabuleiro \n',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
print('Você vai me informar a casa que quer jogar com números.\n E cada um desses números representa as seguintes casas:')
print('00 | 01 | 02\n10 | 11 | 12\n20 | 21 | 22')
print('E aí eu vou lá e substituo a casa pelo seu símbolo, por exemplo:\nO você me informa a seguinte jogada: 22')
print('Eu vou lá e...')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',s2)
print('----------------------------------------------')
#COMEÇO DO JOGO
inicio=sorteio(0,1)
if inicio==0:
    inicio=str('Usuário')
else:
    inicio=str('Máquina')

print('O vencedor do sorteio para incio foi '+inicio)
if inicio=='Usuário':
    print('Então você começa')
    for i in range(9):
        jogada=str(input('Qual a sua jogada '+nome1+'?'))
        print(jogadauser(nome1,tabuleiro,jogada,s1))
        if verificar_vitoria(tabuleiro)==True:
            print('VOCÊ VENCEU')
            break
        print(jogadapc(nome1,s2))
        if verificar_vitoria(tabuleiro)==True:
            print('ahh, não foi dessa vez')
            break
        else:
            continue
        
        
elif inicio=='Máquina':
    print('Então eu começo')
    for i in range(9):
        print(jogadapc(nome1,s2))
        if verificar_vitoria(tabuleiro)==True:
            print('ahh, não foi dessa vez')
            break
        jogada=str(input('Qual a sua jogada '+nome1+'?'))
        print(jogadauser(nome1,tabuleiro,jogada,s1))
        if verificar_vitoria(tabuleiro)==True:
            print('VOCÊ VENCEU')
            break
        else:
            continue