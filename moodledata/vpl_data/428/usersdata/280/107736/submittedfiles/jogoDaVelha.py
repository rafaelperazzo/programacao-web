from jogoDaVelha_BIB import solicitaSimboloDoHumano
from jogoDaVelha_BIB import sorteioPrimeiraJogada
from jogoDaVelha_BIB import jogadaComputador
from jogoDaVelha_BIB import validaJogada
from jogoDaVelha_BIB import jogadaHumana
from jogoDaVelha_BIB import mostraTabuleiro
from jogoDaVelha_BIB import verificaVencedor
from jogoDaVelha_BIB import verificavelha
import sys
import time

print("---------------------------------------")
print("      Bem vindo ao jogo da velha!" )
print("Equipe: A. Marcos, Nelson, Pedro, Renan")
print("---------------------------------------")
time.sleep(2.5)
nome = str(input("Qual o seu nome (ou apelido)?: " ))
pts_jogador = 0
pts_pc = 0
velhas = 0
while(True):
    name=[" ","PC"]
    tab=[[" "," "," "], [" "," "," "], [" "," "," "]]

    name[0]=nome
    si=str(input("Qual símbolo você deseja utilizar no jogo? "))
    simb=solicitaSimboloDoHumano(si)
    print("Sorteando...")
    time.sleep(2)
    jog_1=sorteioPrimeiraJogada(name)
    jog_2=str(" ")
    if jog_1==name[0]:
        jog_2=name[1]
    if jog_1==name[1]:
        jog_2=name[0]
    order=[jog_1, jog_2]
    print("Vencedor do sorteio para início do jogo: %s " %(jog_1))

    cont=0

    for i in range (0,9,1):
        if cont%2==0:
            if order[0] == "PC":
                time.sleep(0.5)
                print("Jogada do PC: ")
                tab=jogadaComputador(simb[1], tab)
                time.sleep(1.5)
                mostraTabuleiro(tab)
                win=verificaVencedor(tab,simb,name)
                if win==True:
                    pts_pc += 1
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
                        velhas += 1
                        break
                    if velha==0:
                        cont = cont + 1
            if order[0] == name[0]:
                play=int(input("Qual a sua jogada, %s? " %(name[0])))
                vplay=validaJogada(play, tab, name,)
                tab=jogadaHumana(vplay,simb,tab)
                mostraTabuleiro(tab)
                win=verificaVencedor(tab,simb,name)
                if win==True:
                    pts_jogador += 1
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
                        velhas += 1
                        break
                    if velha==0:
                        cont = cont + 1
        if cont%2 != 0:
            if order[0] == "PC":
                play=int(input("Qual a sua jogada, %s? " %(name[0])))
                vplay=validaJogada(play, tab, name,)
                tab=jogadaHumana(vplay,simb,tab)
                mostraTabuleiro(tab)
                win=verificaVencedor(tab,simb,name)
                if win==True:
                    pts_jogador += 1
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
                        velhas += 1
                        break
                    if velha==0:
                        cont = cont + 1
            if order[0] == name[0]:
                print("Jogada do PC: ")
                tab=jogadaComputador(simb[1], tab)
                mostraTabuleiro(tab)
                win=verificaVencedor(tab,simb,name)
                if win==True:
                    pts_pc += 1
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
                        velhas += 1
                        break
                    if velha==0:
                        cont = cont + 1
    print('\n')
    print('-------- PLACAR --------')
    print('%s: {%d} | PC: {%d} | Velhas: {%d}'%((nome),(pts_jogador),(pts_pc),(velhas)))
    print('------------------------')


    while (True):
        reiniciar = input("\nJogar novamente, %s? Digite 's' para sim ou 'n' para não: "%(nome))
        if reiniciar in ('s', 'n', '"s"', '"n"'):
            break
        print('\nResposta inválida!')
    if reiniciar == 's' or reiniciar == '"s"':
        print('\n-------------------------------------------------')
        continue
    else:
        print("Até Mais!")
        sys.exit(0)