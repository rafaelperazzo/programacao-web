# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
from random import choice                     #Importa a função "choice" da biblioteca "random"
from os import system                         #Importa a função "system" da biblioteca "os"


class Humano(object): #Classe que cria o nosso objeto "Humano", que será um dos jogadores do jogo
    def __init__(self, nome, simb): #Função que inicializa o objeto criado, atribuindo-lhe nome e símbolo escolhidos
        self.nome = nome
        self.simb = simb

    def jogadaHumana(self, cel): #Função que irá processar a jogada feita pelo nosso jogador Humano
        global jog_val_hum
        self.par_cel = cel
        jog_val_hum.append(self.par_cel)

        

class Computador(object): #Classe que cria o nosso objeto "Computador", que será o outro jogador
    def __init__(self, simb_hum, level): #Função que constrói o nosso "Computador",
        self.nome = "Computador"
        self.level = level
        if simb_hum == 'X': #Atribui ao computador o símbolo restante, após a escolha do símbolo do usuário
            self.simb = 'O'
        else:
            self.simb = 'X'

    def jogadaComputador(self, level): #Função que irá processar a jogada feita pelo nosso Computador
        global jog_val_hum, jog_val_comp, jog_poss, jog_poss_win
        if level == 1:
            self.par_cel = choice(jog_poss)

        if level == 2:
            self.par_cel = choice(jog_poss)
            K = [[], [], [], [], [], [], [], []]
            for j in jog_poss_win[0]:
                if j not in jog_val_hum:
                        K[0].append(j)
                        
            for j in jog_poss_win[1]:
                if j not in jog_val_hum:
                        K[1].append(j)

            for j in jog_poss_win[2]:
                if j not in jog_val_hum:
                        K[2].append(j)

            for j in jog_poss_win[3]:
                if j not in jog_val_hum:
                        K[3].append(j)

            for j in jog_poss_win[4]:
                if j not in jog_val_hum:
                        K[4].append(j)

            for j in jog_poss_win[5]:
                if j not in jog_val_hum:
                        K[5].append(j)

            for j in jog_poss_win[6]:
                if j not in jog_val_hum:
                        K[6].append(j)

            for j in jog_poss_win[7]:
                if j not in jog_val_hum:
                        K[7].append(j)
                        
            for k in K:
                if (len(k) == 1) and (k[0] not in jog_val_comp):
                    self.par_cel = k[0]

        

class Coord(object): #Classe que cria o nosso objeto "Robô Coordenador", que irá realizar as verificações e validações de jogadas
    def __init__(self): #Função que inicializa algum objeto dessa classe ao criarmos
        self.nome = "Robô Coordenador"
        self.cont = 0

    def sorteioPrimeiraJogada(self, nome_hum, nome_comp): #Função que sorteia quem será o primeiro a jogar
        self.nome_hum = nome_hum
        self.nome_comp = nome_comp
        nomes = [self.nome_hum, self.nome_comp] #Lista com os nomes do Humano e do Computador
        self.primeiro = choice(nomes) #Função que "sorteia" algum dos nomes da lista "nomes"
        return self.primeiro

    def solicitaSimboloDoHumano(self): #Função que solicita um símbolo do humano e verifica se este é válido
        self.simb_hum = str(input("Insira o símbolo de sua preferência (X ou O): "))
        while True: #Loop para forçar o usuário a digitar um símbolo válido: "X" ou "O"
            if (self.simb_hum == "X") or (self.simb_hum == "x") or (self.simb_hum == "O") or (self.simb_hum == "o"):
                break
            self.simb_hum = str(input("Símbolo inválido! Digite novamente: "))
        self.simb_hum = self.simb_hum.upper() #Função que converte o símbolo escolhido para maiúsculo, caso seja necessário

    def solicitaLevel(self): #Função que solicita o level de dificuldade e verifica se este mesmo é válido
        self.level = int(input("Selecione o level de dificuldade (1 - Fácil     2 - Médio     3 - Difícil): "))
        while True:
            if (self.level == 1) or (self.level == 2) or (self.level == 3):
                break
            self.level = int(input("Level inválido! Digite novamente: "))

    def validaJogada(self, cel):
        self.cel = cel
        self.cel = str(self.cel)
        self.cel_x = int(self.cel[0])
        self.cel_y = int(self.cel[1])
        self.par_cel = (self.cel_x, self.cel_y)
        global jog_val_hum, jog_val_comp
        while True:
            if (0<=self.cel_x<=2) and (0<=self.cel_y<=2) and (len(self.cel) == 2) and (self.par_cel not in jog_val_hum) and (self.par_cel not in jog_val_comp):
                break
            self.cel = str(input("Jogada inválida! Digite novamente: "))
            self.cel_x = int(self.cel[0])
            self.cel_y = int(self.cel[1])
            self.par_cel = (self.cel_x, self.cel_y)

    def validaJogadaComp(self, par_cel):
        self.par_cel_comp = par_cel
        global jog_val_hum, jog_val_comp, jog_poss
        while True:
            if (self.par_cel_comp not in jog_val_hum) and (self.par_cel_comp not in jog_val_comp):
                break
            self.par_cel_comp = choice(jog_poss)
        jog_val_comp.append(self.par_cel_comp)

    def verificaVencedor(self, nome_hum):
        global jog_val_hum, jog_val_comp
        if (((0,0) in jog_val_hum) and ((0,1) in jog_val_hum) and ((0,2) in jog_val_hum)) or (((1,0) in jog_val_hum) and ((1,1) in jog_val_hum) and ((1,2) in jog_val_hum)) or (((2,0) in jog_val_hum) and ((2,1) in jog_val_hum) and ((2,2) in jog_val_hum)):
            print("Vencedor: %s!\n"%nome_hum)
            self.cont = 1
            
        elif (((0,0) in jog_val_hum) and ((1,0) in jog_val_hum) and ((2,0) in jog_val_hum)) or (((0,1) in jog_val_hum) and ((1,1) in jog_val_hum) and ((2,1) in jog_val_hum)) or (((0,2) in jog_val_hum) and ((1,2) in jog_val_hum) and ((2,2) in jog_val_hum)):
            print("Vencedor: %s!\n"%nome_hum)
            self.cont = 1

        elif (((0,0) in jog_val_hum) and ((1,1) in jog_val_hum) and ((2,2) in jog_val_hum)) or (((0,2) in jog_val_hum) and ((1,1) in jog_val_hum) and ((2,0) in jog_val_hum)):
            print("Vencedor: %s!\n"%nome_hum)
            self.cont = 1

        elif (((0,0) in jog_val_comp) and ((0,1) in jog_val_comp) and ((0,2) in jog_val_comp)) or (((1,0) in jog_val_comp) and ((1,1) in jog_val_comp) and ((1,2) in jog_val_comp)) or (((2,0) in jog_val_comp) and ((2,1) in jog_val_comp) and ((2,2) in jog_val_comp)):
            print("Vencedor: Computador!\n")
            self.cont = 1

        elif (((0,0) in jog_val_comp) and ((1,0) in jog_val_comp) and ((2,0) in jog_val_comp)) or (((0,1) in jog_val_comp) and ((1,1) in jog_val_comp) and ((2,1) in jog_val_comp)) or (((0,2) in jog_val_comp) and ((1,2) in jog_val_comp) and ((2,2) in jog_val_comp)):
            print("Vencedor: Computador!\n")
            self.cont = 1

        elif (((0,0) in jog_val_comp) and ((1,1) in jog_val_comp) and ((2,2) in jog_val_comp)) or (((0,2) in jog_val_comp) and ((1,1) in jog_val_comp) and ((2,0) in jog_val_comp)):
            print("Vencedor: Computador!\n")
            self.cont = 1

        else:
            if len(jog_val_hum) + len(jog_val_comp) == 9:
                print("Deu velha!!!\n")
                self.cont = 1


class Tabuleiro(object):
    def __init__(self):
        self.a00, self.a01, self.a02, self.a10, self.a11, self.a12, self.a20, self.a21, self.a22 = " ", " ", " ", " ", " ", " ", " ", " ", " "

    def mostraTabuleiro(self, simb_hum, simb_comp, player, par_cel):
        if player == 'Humano':
            if par_cel == (0,0):
                self.a00 = simb_hum
                
            elif par_cel == (0,1):
                self.a01 = simb_hum
                
            elif par_cel == (0,2):
                self.a02 = simb_hum

            elif par_cel == (1,0):
                self.a10 = simb_hum

            elif par_cel == (1,1):
                self.a11 = simb_hum

            elif par_cel == (1,2):
                self.a12 = simb_hum

            elif par_cel == (2,0):
                self.a20 = simb_hum

            elif par_cel == (2,1):
                self.a21 = simb_hum

            else:
                self.a22 = simb_hum

        else:
            if par_cel == (0,0):
                self.a00 = simb_comp
                
            elif par_cel == (0,1):
                self.a01 = simb_comp
                
            elif par_cel == (0,2):
                self.a02 = simb_comp

            elif par_cel == (1,0):
                self.a10 = simb_comp

            elif par_cel == (1,1):
                self.a11 = simb_comp

            elif par_cel == (1,2):
                self.a12 = simb_comp

            elif par_cel == (2,0):
                self.a20 = simb_comp

            elif par_cel == (2,1):
                self.a21 = simb_comp

            else:
                self.a22 = simb_comp
                
        print("\n\n" + self.a00 + '|' + self.a01 + '|' + self.a02       )
        print(         self.a10 + '|' + self.a11 + '|' + self.a12       )
        print(         self.a20 + '|' + self.a21 + '|' + self.a22 + "\n")

