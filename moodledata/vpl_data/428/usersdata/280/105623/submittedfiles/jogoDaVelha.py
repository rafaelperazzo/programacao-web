from jogoDaVelha_BIB import solicitaSimboloDoHumano
from jogoDaVelha_BIB import sorteioPrimeiraJogada
from jogoDaVelha_BIB import jogadaComputador
from jogoDaVelha_BIB import validaJogada
from jogoDaVelha_BIB import jogadaHumana
from jogoDaVelha_BIB import mostraTabuleiro
from jogoDaVelha_BIB import verificaVencedor
from jogoDaVelha_BIB import verificavelha
import sys
while(True):
    name=[" ","PC"]
    tab=[[" "," "," "], [" "," "," "], [" "," "," "]]


    print("Bem vindo ao jogo da velha!" )
    nome = str(input("Qual o seu nome (ou apelido)?: " ))
    name[0]=nome
    si=str(input("Qual símbolo você deseja utilizar no jogo? "))
    simb=solicitaSimboloDoHumano(si)
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
                print("Jogada do PC: ")
                tab=jogadaComputador(simb[1], tab)
                mostraTabuleiro(tab)
                win=verificaVencedor(tab,simb,name)
                if win==True:
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
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
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
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
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
                        break
                    if velha==0:
                        cont = cont + 1
            if order[0] == name[0]:
                print("Jogada do PC: ")
                tab=jogadaComputador(simb[1], tab)
                mostraTabuleiro(tab)
                win=verificaVencedor(tab,simb,name)
                if win==True:
                    break
                if win==False:
                    velha=verificavelha(tab)
                    if velha != 0:
                        break
                    if velha==0:
                        cont = cont + 1

    while (True):
        reiniciar = input("\nJogar novamente? Digite 's' para sim ou 'n' para não: ")
        if reiniciar in ('s', 'n', '"s"', '"n"'):
            break
        print('\nResposta inválida!')
    if reiniciar == 's' or reiniciar == '"s"':
        print('\n-------------------------------------------------')
        continue
    else:
        print("Até Mais!")
        sys.exit(0)