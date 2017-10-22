# -*- coding: utf-8 -*-

from jogoDaVelha_BIB import *
nome = str(input("Digite o seu nome: "))
cont = " "
while True:
    global jog_val_hum, jog_val_comp, jog_poss, jog_poss_win    #Define duas listas que armazenarão as jogadas como globais
    jog_val_hum = []                                            #Lista que irá guardar as jogadas do nosso player Humano
    jog_val_comp = []                                           #Lista que irá guardar as jogadas do nosso player Computador
    jog_poss = ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2))
    jog_poss_win = (((0,0),(0,1),(0,2)),((1,0),(1,1),(1,2)),((2,0),(2,1),(2,2)),((0,0),(1,0),(2,0)),((0,1),(1,1),(2,1)),((0,2),(1,2),(2,2)),((0,0),(1,1),(2,2)),((2,0),(1,1),(0,2)))
    cont2 = 0
    Juiz = Coord()
    Tab = Tabuleiro()
    Juiz.solicitaSimboloDoHumano()
    Juiz.solicitaLevel()
    Player = Humano(nome, Juiz.simb_hum)
    Comp = Computador(Player.simb, Juiz.level)
    Juiz.sorteioPrimeiraJogada(Player.nome, Comp.nome)
    print("O primeiro jogador sera o %s!\n"%Juiz.primeiro)
    if Juiz.primeiro == Player.nome:
        while True:
            jog = str(input("Digite a sua jogada, %s: "%Player.nome))
            Juiz.validaJogada(jog)
            Player.jogadaHumana(Juiz.par_cel)
            Tab.mostraTabuleiro(Player.simb, Comp.simb, "Humano", Player.par_cel)
            Juiz.verificaVencedor(Player.nome)
            if Juiz.cont == 1:
                break
            Comp.jogadaComputador(Comp.level)
            Juiz.validaJogadaComp(Comp.par_cel)
            Tab.mostraTabuleiro(Player.simb, Comp.simb, "Computador", Juiz.par_cel_comp)
            Juiz.verificaVencedor(Player.nome)
            if Juiz.cont == 1:
                break

    else:
        while True:
            Comp.jogadaComputador(Comp.level)
            Juiz.validaJogadaComp(Comp.par_cel)
            Tab.mostraTabuleiro(Player.simb, Comp.simb, "Computador", Juiz.par_cel_comp)
            Juiz.verificaVencedor(Player.nome)
            if Juiz.cont == 1:
                break
            jog = str(input("Digite a sua jogada, %s: "%Player.nome))
            Juiz.validaJogada(jog)
            Player.jogadaHumana(Juiz.par_cel)
            Tab.mostraTabuleiro(Player.simb, Comp.simb, "Humano", Player.par_cel)
            Juiz.verificaVencedor(Player.nome)
            if Juiz.cont == 1:
                break
    cont = str(input("Deseja continuar?: "))
    while True:
        if cont == 's' or cont == 'S' or cont == 'sim' or cont == 'Sim' or cont == 'sIm' or cont == 'siM' or cont == 'SIm' or cont == 'sIM' or cont == 'SiM' or cont == 'SIM':
            break
        
        if cont == 'n' or cont == 'N' or cont == 'nao' or cont == 'Nao' or cont == 'nAo' or cont == 'naO' or cont == 'NAo' or cont == 'nAO' or cont == 'NaO' or cont == 'NAO':
            break
        
        if cont == 'não' or cont == 'Não' or cont == 'nÃo' or cont == 'nãO' or cont == 'NÃo' or cont == 'nÃO' or cont == 'NãO' or cont == 'NÃO':
            break
        
        cont = str(input("Opção inválida! Digite novamente: "))
        
    if cont == 'n' or cont == 'N' or cont == 'nao' or cont == 'Nao' or cont == 'nAo' or cont == 'naO' or cont == 'NAo' or cont == 'nAO' or cont == 'NaO' or cont == 'NAO':
        break

    if cont == 'não' or cont == 'Não' or cont == 'nÃo' or cont == 'nãO' or cont == 'NÃo' or cont == 'nÃO' or cont == 'NãO' or cont == 'NÃO':
        break
