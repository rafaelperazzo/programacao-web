###################################################### -   Módulos   - ##################################################################
import time                                   #Importa o módulo "time"
from random import choice                     #Importa a função "choice" do módulo "random"
import os                                     #Importa o módulo "os"


###################################################### -   Classes   - ##################################################################
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
        if level == 1: #No level 1(Fácil), o computador simplesmente escolhe as jogadas dele aleatoriamente
            self.par_cel = choice(jog_poss)

        if level == 2: #No level 2(Médio), o computador analisa a jogada do adversário e tenta impedir que ele ganhe, mas ainda não tem o objetivo de vencer
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
                if (len(k) == 1) and (k[0] not in jog_val_comp) and (k[0] not in jog_val_hum):
                    self.par_cel = k[0]

        if level == 3: #No level 3(Difícil), o Computador começa a se tornar agressivo, priorizando completar as casas que faltarem para ele ganhar
            self.par_cel = (1,1)
            K = [[], [], [], [], [], [], [], [],[], [], [], [], [], [], [], []]
            for i in range(1,2):
                for j in jog_poss_win[0]:
                    if j not in jog_val_comp:
                            K[0].append(j)
                            
                for j in jog_poss_win[1]:
                    if j not in jog_val_comp:
                            K[1].append(j)

                for j in jog_poss_win[2]:
                    if j not in jog_val_comp:
                            K[2].append(j)

                for j in jog_poss_win[3]:
                    if j not in jog_val_comp:
                            K[3].append(j)

                for j in jog_poss_win[4]:
                    if j not in jog_val_comp:
                            K[4].append(j)

                for j in jog_poss_win[5]:
                    if j not in jog_val_comp:
                            K[5].append(j)

                for j in jog_poss_win[6]:
                    if j not in jog_val_comp:
                            K[6].append(j)

                for j in jog_poss_win[7]:
                    if j not in jog_val_comp:
                            K[7].append(j)
                            
                for k in K:
                    if (len(k) == 1) and (k[0] not in jog_val_comp) and (k[0] not in jog_val_hum):
                        self.par_cel = k[0]
                        
                self.par_cel_list = [self.par_cel]

                if self.par_cel_list in K:
                    continue
                    
                for j in jog_poss_win[0]:
                    if j not in jog_val_hum:
                            K[8].append(j)
                            
                for j in jog_poss_win[1]:
                    if j not in jog_val_hum:
                            K[9].append(j)

                for j in jog_poss_win[2]:
                    if j not in jog_val_hum:
                            K[10].append(j)

                for j in jog_poss_win[3]:
                    if j not in jog_val_hum:
                            K[11].append(j)

                for j in jog_poss_win[4]:
                    if j not in jog_val_hum:
                            K[12].append(j)

                for j in jog_poss_win[5]:
                    if j not in jog_val_hum:
                            K[13].append(j)

                for j in jog_poss_win[6]:
                    if j not in jog_val_hum:
                            K[14].append(j)

                for j in jog_poss_win[7]:
                    if j not in jog_val_hum:
                            K[15].append(j)
                            
                for k in K:
                    if (len(k) == 1) and (k[0] not in jog_val_comp) and (k[0] not in jog_val_hum):
                        self.par_cel = k[0]

        if level == 4: #No level 4(Profissional), o Computador sempre irá na direção das jogadas que encurralam o adversário, além de nunca deixá-lo vencer!
            self.par_cel = (1,1)
            K = [[], [], [], [], [], [], [], [],[], [], [], [], [], [], [], []]
            h = len(jog_val_hum)
            c = len(jog_val_comp)
            for i in range(1,2):
                #Início 1º Caso: PC começa e Humano joga em canto (0,0)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (0,0)):
                    self.par_cel = (2,2)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (0,0)) and (jog_val_hum[1] == (1,2)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (2,2)):
                    self.par_cel = (2,0)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (0,0)) and (jog_val_hum[1] == (2,1)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (2,2)):
                    self.par_cel = (0,2)
                    continue
                #Fim 1º caso

                #Início 2º Caso: PC começa e Humano joga em canto (0,2)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (0,2)):
                    self.par_cel = (2,0)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (0,2)) and (jog_val_hum[1] == (2,1)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (2,0)):
                    self.par_cel = (0,0)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (0,2)) and (jog_val_hum[1] == (1,0)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (2,0)):
                    self.par_cel = (2,2)
                    continue
                #Fim 2º Caso

                #Início 3º Caso: PC começa e Humano joga em canto (2,2)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (2,2)):
                    self.par_cel = (0,0)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (2,2)) and (jog_val_hum[1] == (0,1)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (0,0)):
                    self.par_cel = (2,0)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (2,2)) and (jog_val_hum[1] == (1,0)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (0,0)):
                    self.par_cel = (0,2)
                    continue
                #Fim 3º Caso

                #Início 4º Caso: PC começa e Humano joga em canto (2,0)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (2,0)):
                    self.par_cel = (0,2)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (2,0)) and (jog_val_hum[1] == (0,1)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (0,2)):
                    self.par_cel = (2,2)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (2,0)) and (jog_val_hum[1] == (1,2)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (0,2)):
                    self.par_cel = (0,0)
                    continue
                #Fim 4º Caso

                #Início 5º Caso: PC começa e Humano joga em lado (0,1)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (0,1)):
                    self.par_cel = (0,0)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (0,1)) and (jog_val_hum[1] == (2,2)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (0,0)):
                    self.par_cel = (2,0)
                    continue
                #Fim 5º Caso

                #Início 6º Caso: PC começa e Humano joga em lado (1,2)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (1,2)):
                    self.par_cel = (0,2)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (1,2)) and (jog_val_hum[1] == (2,0)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (0,2)):
                    self.par_cel = (0,0)
                    continue
                #Fim 6º Caso

                #Início 7º Caso: PC começa e Humano joga em lado (2,1)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (2,1)):
                    self.par_cel = (2,2)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (2,1)) and (jog_val_hum[1] == (0,0)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (2,2)):
                    self.par_cel = (0,2)
                    continue
                #Fim 7º Caso

                #Início 8º Caso: PC começa e Humano joga em lado (1,0)
                if (h == 1) and (c == 1) and (jog_val_comp[0] == (1,1)) and (jog_val_hum[0] == (1,0)):
                    self.par_cel = (2,0)
                    continue

                if (h == 2) and (c == 2) and (jog_val_hum[0] == (1,0)) and (jog_val_hum[1] == (0,2)) and (jog_val_comp[0] == (1,1)) and (jog_val_comp[1] == (2,0)):
                    self.par_cel = (2,2)
                    continue
                #Fim 8º Caso

                #Início 9º Caso: Humano começa e joga no meio (1,1)
                if (h == 1) and (jog_val_hum[0] == (1,1)):
                    self.par_cel = (0,0)
                    continue

                if (h == 2) and (c == 1) and (jog_val_hum[0] == (1,1)) and (jog_val_hum[1] == (2,2)) and (jog_val_comp[0] == (0,0)):
                    self.par_cel = (0,2)
                    continue
                #Fim 9º Caso

                #Início 10º Caso: Humano começa e joga no lado (0,1)
                if (h == 2) and (jog_val_hum[0] == (0,1)):
                    if (jog_val_hum[1] == (1,0)) or (jog_val_hum[1] == (2,0)):
                        self.par_cel = (0,0)
                        continue
                        
                    if (jog_val_hum[1] == (1,2)) or (jog_val_hum[1] == (2,2)):
                        self.par_cel = (0,2)
                        continue

                if (h == 2) and ((0,1) in jog_val_hum) and ((2,1) in jog_val_hum):
                    self.par_cel = (0,0)
                    continue
                #Fim 10º Caso

                #Início 11º Caso: Humano começa e joga no lado (1,2)
                if (h == 2) and (jog_val_hum[0] == (1,2)):
                    if (jog_val_hum[1] == (0,1)) or (jog_val_hum[1] == (0,0)):
                        self.par_cel = (0,2)
                        continue
                        
                    if (jog_val_hum[1] == (2,1)) or (jog_val_hum[1] == (2,0)):
                        self.par_cel = (2,2)
                        continue

                if (h == 2) and ((1,2) in jog_val_hum) and ((1,0) in jog_val_hum):
                    self.par_cel = (0,2)
                    continue
                #Fim 11º Caso

                #Início 12º Caso: Humano começa e joga no lado (1,0)
                if (h == 2) and (jog_val_hum[0] == (1,0)):
                    if (jog_val_hum[1] == (0,1)) or (jog_val_hum[1] == (0,2)):
                        self.par_cel = (0,0)
                        continue

                    if (jog_val_hum[1] == (2,1)) or (jog_val_hum[1] == (2,2)):
                        self.par_cel = (2,0)
                        continue
                #Fim 12º Caso

                #Início 13º Caso: Humano começa e joga no lado (2,1)
                if (h == 2) and (jog_val_hum[0] == (2,1)):
                    if (jog_val_hum[1] == (1,2)) or (jog_val_hum[1] == (0,2)):
                        self.par_cel = (2,2)
                        continue

                    if (jog_val_hum[1] == (1,0)) or (jog_val_hum[1] == (0,0)):
                        self.par_cel = (2,0)
                        continue
                #Fim 13º Caso

                #Início 14º Caso: Humano começa e joga no canto (0,0)
                if (h == 2) and (jog_val_hum[0] == (0,0)):
                    if (jog_val_hum[1] == (1,2)):
                        self.par_cel = (0,2)
                        continue

                    if (jog_val_hum[1] == (2,1)):
                        self.par_cel = (2,0)
                        continue

                if (h == 2) and ((0,0) in jog_val_hum) and ((2,2) in jog_val_hum):
                    self.par_cel = (1,0)
                    continue
                #Fim 14º Caso

                #Início 15º Caso: Humano começa e joga no canto (0,2)
                if (h == 2) and (jog_val_hum[0] == (0,2)):
                    if (jog_val_hum[1] == (1,0)):
                        self.par_cel = (0,0)
                        continue

                    if (jog_val_hum[1] == (2,1)):
                        self.par_cel = (2,2)
                        continue

                if (h == 2) and ((0,2) in jog_val_hum) and ((2,0) in jog_val_hum):
                    self.par_cel = (0,1)
                    continue
                #Fim 15º Caso

                #Início 16º Caso: Humano começa e joga no canto (2,2)
                if (h == 2) and (jog_val_hum[0] == (2,2)):
                    if (jog_val_hum[1] == (0,1)):
                        self.par_cel = (0,2)
                        continue

                    if (jog_val_hum[1] == (1,0)):
                        self.par_cel = (2,0)
                        continue
                #Fim 16º Caso

                #Início 17º Caso: Humano começa e joga no canto (2,0)
                if (h == 2) and (jog_val_hum[0] == (2,0)):
                    if (jog_val_hum[1] == (0,1)):
                        self.par_cel = (0,0)
                        continue

                    if (jog_val_hum[1] == (1,2)):
                        self.par_cel = (2,2)
                        continue
                #Fim 17º Caso
                
                for j in jog_poss_win[0]:
                    if j not in jog_val_comp:
                            K[0].append(j)
                            
                for j in jog_poss_win[1]:
                    if j not in jog_val_comp:
                            K[1].append(j)

                for j in jog_poss_win[2]:
                    if j not in jog_val_comp:
                            K[2].append(j)

                for j in jog_poss_win[3]:
                    if j not in jog_val_comp:
                            K[3].append(j)

                for j in jog_poss_win[4]:
                    if j not in jog_val_comp:
                            K[4].append(j)

                for j in jog_poss_win[5]:
                    if j not in jog_val_comp:
                            K[5].append(j)

                for j in jog_poss_win[6]:
                    if j not in jog_val_comp:
                            K[6].append(j)

                for j in jog_poss_win[7]:
                    if j not in jog_val_comp:
                            K[7].append(j)
                            
                for k in K:
                    if (len(k) == 1) and (k[0] not in jog_val_comp) and (k[0] not in jog_val_hum):
                        self.par_cel = k[0]
                        
                self.par_cel_list = [self.par_cel]

                if self.par_cel_list in K:
                    continue
                    
                for j in jog_poss_win[0]:
                    if j not in jog_val_hum:
                            K[8].append(j)
                            
                for j in jog_poss_win[1]:
                    if j not in jog_val_hum:
                            K[9].append(j)

                for j in jog_poss_win[2]:
                    if j not in jog_val_hum:
                            K[10].append(j)

                for j in jog_poss_win[3]:
                    if j not in jog_val_hum:
                            K[11].append(j)

                for j in jog_poss_win[4]:
                    if j not in jog_val_hum:
                            K[12].append(j)

                for j in jog_poss_win[5]:
                    if j not in jog_val_hum:
                            K[13].append(j)

                for j in jog_poss_win[6]:
                    if j not in jog_val_hum:
                            K[14].append(j)

                for j in jog_poss_win[7]:
                    if j not in jog_val_hum:
                            K[15].append(j)
                            
                for k in K:
                    if (len(k) == 1) and (k[0] not in jog_val_comp) and (k[0] not in jog_val_hum):
                        self.par_cel = k[0]

            

class Coord(object): #Classe que cria o nosso objeto "Robô Coordenador", que irá realizar as verificações e validações de jogadas
    def __init__(self): #Função que inicializa algum objeto dessa classe ao criarmos
        nome = "Robô Coordenador"
        self.cont = 0

    def sorteioPrimeiraJogada(self, nome_hum, nome_comp, level): #Função que sorteia quem será o primeiro a jogar de acordo com o level
        self.nome_hum = nome_hum
        self.nome_comp = nome_comp
        sec = int(time.asctime()[17] + time.asctime()[18]) #Define a variável 'sec', que é os segundos do exato instante em que a variável for "posta em ação"
        if (level == 1) or (level == 2): #Para os levels Fácil e Médio, há 50% de chance de cada um ser selecionado, visto que entre [0,60), metade dos números
            if (sec%2 == 0):             #são pares e metade ímpares, além de estarem distribuídos uniformemente nesse intervalo
                self.primeiro = self.nome_hum

            else:
                self.primeiro = self.nome_comp
            
        else:                #Para os levels Difícil e Profissional, há apenas 25% de chance do jogador Humano ser selecionado, enquanto há 75% de chance do
            if (sec%4 == 0): #computador ser selecionado como primeiro, visto que somente 25% dos números em [0,60) são divisíveis por 4
                self.primeiro = self.nome_hum

            else:
                self.primeiro = self.nome_comp

    def solicitaSimboloDoHumano(self): #Função que solicita um símbolo do humano e verifica se este é válido
        self.simb_hum = str(input("Insira o símbolo de sua preferência (X ou O): "))
        while True: #Loop para forçar o usuário a digitar um símbolo válido: "X" ou "O"
            if (self.simb_hum == "X") or (self.simb_hum == "x") or (self.simb_hum == "O") or (self.simb_hum == "o"):
                break
            self.simb_hum = str(input("Símbolo inválido! Digite novamente: "))
        self.simb_hum = self.simb_hum.upper() #Função que converte o símbolo escolhido para maiúsculo, caso seja necessário

    def solicitaLevel(self): #Função que solicita o level de dificuldade e verifica se este mesmo é válido
        cont = 0
        while True:
            try: #O 'try' é o statement que tenta executar um bloco de código
                if (cont == 0):
                    cont = 1
                    self.level = int(input("Selecione o level de dificuldade (1 - Fácil     2 - Médio     3 - Difícil     4 - Profissional): "))
                    cont = 2

                if (cont == 1):
                    self.level = int(input("Caractere inválido! Digite novamente: "))
                    cont = 2

            except: #Caso a execução do bloco 'try' apresente algum erro, ao invés de fechar o programa, ele entra no bloco 'except'
                continue

            if cont == 2:
                break

        
        while True:
            if (self.level == 1) or (self.level == 2) or (self.level == 3) or (self.level == 4):
                break

            cont = 0
            while True:
                try:
                    if (cont == 0):
                        cont = 1
                        self.level = int(input("Level inválido! Digite novamente: "))
                        cont = 2

                    if (cont == 1):
                        self.level = int(input("Caractere inválido! Digite novamente: "))
                        cont = 2

                except:
                    continue

                if cont == 2:
                    break

    def validaJogada(self, cel): #Função que verifica se a jogada do Humano é válida
        cont = 0
        while cont != 1:
            self.cel = ""
            
            for i in cel.split():
                self.cel += i

            try:
                self.cel_x = int(self.cel[0])
                self.cel_y = int(self.cel[1])
                cont = 1

            except:
                cel = str(input("Jogada inválida! Digite novamente: "))

        self.par_cel = (self.cel_x, self.cel_y)
        global jog_val_hum, jog_val_comp
        while True:
            if (0<=self.cel_x<=2) and (0<=self.cel_y<=2) and (len(self.cel) == 2) and (self.par_cel not in jog_val_hum) and (self.par_cel not in jog_val_comp):
                break

            cont = 0
            cel = str(input("Jogada inválida! Digite novamente: "))
            
            while cont != 1:
                self.cel = ""
                for i in cel.split():
                    self.cel += i

                try:    
                    self.cel_x = int(self.cel[0])
                    self.cel_y = int(self.cel[1])
                    cont = 1

                except:
                    cel = str(input("Jogada inválida! Digite novamente: "))
                    
            self.par_cel = (self.cel_x, self.cel_y)

    def validaJogadaComp(self, par_cel): #Função que verifica se a jogada do Computador é válida
        self.par_cel_comp = par_cel
        global jog_val_hum, jog_val_comp, jog_poss
        while True:
            if (self.par_cel_comp not in jog_val_hum) and (self.par_cel_comp not in jog_val_comp):
                break
            self.par_cel_comp = choice(jog_poss)
        jog_val_comp.append(self.par_cel_comp)

    def verificaVencedor(self, nome_hum): #Função para verificar, a cada jogada realizada, se há um vencedor
        global jog_val_hum, jog_val_comp
        
        #Início das condições de verificação para o caso em que o HUMANO vença 
        if ((((0,0) in jog_val_hum) and ((0,1) in jog_val_hum) and ((0,2) in jog_val_hum)) or
            (((1,0) in jog_val_hum) and ((1,1) in jog_val_hum) and ((1,2) in jog_val_hum)) or
            (((2,0) in jog_val_hum) and ((2,1) in jog_val_hum) and ((2,2) in jog_val_hum))):
            print("Vencedor: %s!\n"%nome_hum)
            self.cont = 1
            
        elif ((((0,0) in jog_val_hum) and ((1,0) in jog_val_hum) and ((2,0) in jog_val_hum)) or
              (((0,1) in jog_val_hum) and ((1,1) in jog_val_hum) and ((2,1) in jog_val_hum)) or
              (((0,2) in jog_val_hum) and ((1,2) in jog_val_hum) and ((2,2) in jog_val_hum))):
            print("Vencedor: %s!\n"%nome_hum)
            self.cont = 1

        elif ((((0,0) in jog_val_hum) and ((1,1) in jog_val_hum) and ((2,2) in jog_val_hum)) or
              (((0,2) in jog_val_hum) and ((1,1) in jog_val_hum) and ((2,0) in jog_val_hum))):
            print("Vencedor: %s!\n"%nome_hum)
            self.cont = 1
        #Fim

        #Início das condições de verificação para o caso em que o COMPUTADOR vença
        elif ((((0,0) in jog_val_comp) and ((0,1) in jog_val_comp) and ((0,2) in jog_val_comp)) or
              (((1,0) in jog_val_comp) and ((1,1) in jog_val_comp) and ((1,2) in jog_val_comp)) or
              (((2,0) in jog_val_comp) and ((2,1) in jog_val_comp) and ((2,2) in jog_val_comp))):
            print("Vencedor: Computador!\n")
            self.cont = 1

        elif ((((0,0) in jog_val_comp) and ((1,0) in jog_val_comp) and ((2,0) in jog_val_comp)) or
              (((0,1) in jog_val_comp) and ((1,1) in jog_val_comp) and ((2,1) in jog_val_comp)) or
              (((0,2) in jog_val_comp) and ((1,2) in jog_val_comp) and ((2,2) in jog_val_comp))):
            print("Vencedor: Computador!\n")
            self.cont = 1

        elif ((((0,0) in jog_val_comp) and ((1,1) in jog_val_comp) and ((2,2) in jog_val_comp)) or
              (((0,2) in jog_val_comp) and ((1,1) in jog_val_comp) and ((2,0) in jog_val_comp))):
            print("Vencedor: Computador!\n")
            self.cont = 1
        #Fim

        #Verificação para o caso em que seja empate
        else:
            if len(jog_val_hum) + len(jog_val_comp) == 9:
                print("Deu velha!!!\n")
                self.cont = 1


class Tabuleiro(object): #Classe que cria o nosso objeto Tabuleiro, que irá exibir as jogadas feitas pelos jogadores 
    def __init__(self): #A função construtora dessa classe atribui ao objeto todas as casas inicialmente como vazias
        self.a00, self.a01, self.a02, self.a10, self.a11, self.a12, self.a20, self.a21, self.a22 = " ", " ", " ", " ", " ", " ", " ", " ", " "

    def mostraTabuleiro(self, simb_hum, simb_comp, player, par_cel): #Função que substitui o espaço vazio correspondente à jogada pelo símbolo do jogador
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
                
        print("\n\n     |     |     ")
        print("  " + self.a00 + "  |  " + self.a01 + "  |  " + self.a02 + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + self.a10 + "  |  " + self.a11 + "  |  " + self.a12 + "  ")
        print("_____|_____|_____")
        print("     |     |     ")
        print("  " + self.a20 + "  |  " + self.a21 + "  |  " + self.a22 + "  ")
        print("     |     |     \n\n")


def clear(case):
    if (case == 1):
        os.system("cls")
        """
        placar = open("placar.txt", "r")
        print(placar.read())
        placar.close()
        """
        print("=========================================================================")
        print("Seja muito bem vindo(a) ao Jogo da Velha do grupo Robotic! Aproveite!")
        print("=========================================================================\n")

    if (case == 2):
        os.system("cls")
        print("=========================================================================")
        print("Seja muito bem vindo(a) ao Jogo da Velha do grupo Robotic! Aproveite!")
        print("=========================================================================")
        print("\n\nCaso queira ler o manual de instruções do jogo, digite '?' no nome.")
        print("-------------------------------------------------------------------------")
        
