import random
from time import sleep

#######################################################################################
def recebe_e_validar_jogada():
    n = input('Digite sua jogada: ')
    i = int(n[0])
    j = int(n[1])
    while(True): 
        if int(n[0]) >= 0 and int(n[0]) < 3 :
            if int(n[1]) >= 0 and int(n[1]) < 3:
                if tabuleiro[i][j] != "X" and tabuleiro[i][j] != "O" :
                    break
        else:
            n = input('Digite uma jogada válida %s: ' % nome_do_jogador)
   

    tabuleiro[i][j] = simb
   
def jogada_do_computador():
    n = random.choice(('00', '21', '02', '10', '11', '12', '22', '20', '01'))
    while(True): 
        i = int(n[0])
        j = int(n[1])
        if tabuleiro[i][j] != "X" and tabuleiro[i][j] != "O" : 
            break
        else:
            n = random.choice(('00', '21', '02', '10', '11', '12', '22', '20', '01'))
    
    tabuleiro[i][j] = simbc
 
def mostre_tabuleiro():
    print(" ")
    print(coordenadas[0][0]  + "|" + coordenadas[0][1] + ' ' + "|" + coordenadas[0][2]) 
    print('---+--+---')
    print(coordenadas[1][0]  + "|" + coordenadas[1][1] + ' ' + "|" + coordenadas[1][2])    #print coordenadas
    print('---+--+---')
    print(coordenadas[2][0]  + "|" + coordenadas[2][1] + ' ' + "|" + coordenadas[2][2])
    sleep(1)
    print(" ")
    print(tabuleiro[0][0] + '  ' + "|" + tabuleiro[0][1] + ' ' + "|" + tabuleiro[0][2]) 
    print('---+--+---')
    print(tabuleiro[1][0] + '  ' + "|" + tabuleiro[1][1] + ' ' + "|" + tabuleiro[1][2])    #print tabuleiro
    print('---+--+---')
    print(tabuleiro[2][0] + '  ' + "|" + tabuleiro[2][1] + ' ' + "|" + tabuleiro[2][2])
    
    

def verifica_vencedor():
    if (tabuleiro[0][0]==tabuleiro[0][1]==tabuleiro[0][2]) and (tabuleiro[0][1] in ['X', 'O']) : 
        return True
    elif (tabuleiro[1][0]==tabuleiro[1][1]==tabuleiro[1][2]) and (tabuleiro[1][1] in ['X', 'O'])  : 
        return True
    elif (tabuleiro[2][0]==tabuleiro[2][1]==tabuleiro[2][2]) and (tabuleiro[2][1] in ['X', 'O'])  :
        return True
    elif (tabuleiro[0][0]==tabuleiro[1][0]==tabuleiro[2][0]) and (tabuleiro[1][0] in ['X', 'O'])  :
        return True
    elif (tabuleiro[0][1]==tabuleiro[1][1]==tabuleiro[2][1]) and (tabuleiro[1][1] in ['X', 'O'])  :
        return True
    elif (tabuleiro[0][2]==tabuleiro[1][2]==tabuleiro[2][2]) and (tabuleiro[1][2] in ['X', 'O'])  :
        return True
    elif (tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]) and (tabuleiro[1][1] in ['X', 'O'])  :
        return True
    elif (tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]) and (tabuleiro[1][1] in ['X', 'O'])  :
        return True 
    else:
        soma = 0
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] != ' ' :
                    soma += 1
    if soma == 9 :
        return 'Velha'

#####################################################################################################################################################################################################################################################################

jn = 's'
while jn == 's' or jn == 'S':

    coordenadas = [
                ('00', '01', '02')
                ,('10', '11','12')  #Matriz das coordenadas
                ,('20','21','22')
                ]
    
    tabuleiro = [
                (' ', ' ', ' ')
                ,(' ', ' ', ' ')  #matriz tabuleiro
                ,(' ', ' ', ' ')
                ]
    tabuleiro = []
    for i in range (3):
        v = []
        for j in range(3):
            v.append(' ')
        tabuleiro.append(v)


    nome_do_jogador = input("Digite o seu nome: ") #Pede o nome do jogador
    simb = input('Digite o simbolo com o qual você deseja jogar %s : ' % nome_do_jogador)
    while(True):   #Verifica se o simbolo é vàlido
        if simb == "X" or simb == "O" :
            break
        else:
            simb = input("Digite um simbolo válido %s : " % nome_do_jogador)
        
    
    if simb == 'X':
        simbc = 'O'
    else:
        simbc = 'X'
    
    print('Agora sortearemos quem começará: ')
    sleep(1.5)
    
    a = (random.choice(('1','2')))
    
    if a == '1':
        print('Você começa: ')
        while(True) :
                mostre_tabuleiro()
                recebe_e_validar_jogada()
                if verifica_vencedor() :
                    if verifica_vencedor() == 'Velha' :
                        print(' ')
                        print('Deu velha')    
                        break
                    else:
                        mostre_tabuleiro()
                        print(' ')
                        print('Você ganhou %s !' % nome_do_jogador)
                        break
                jogada_do_computador()
                if verifica_vencedor() :
                    if verifica_vencedor() == 'Velha' :
                        print(' ')
                        print('Deu velha')
                        break
                    else:
                        mostre_tabuleiro()
                        print(' ')
                        print('O computador ganhou!')
                        break
                    
        
    
    if a == '2' :
        print('O computador começou')
        while(True):
            jogada_do_computador()
            mostre_tabuleiro()
            if verifica_vencedor() :
                if verifica_vencedor() == 'Velha' :
                    print(' ')
                    print('Deu velha')
                    break
                else:
                    mostre_tabuleiro()
                    print(' ')
                    print('O computador ganhou!')
                    break
            recebe_e_validar_jogada()
            if verifica_vencedor() :
                if verifica_vencedor() == 'Velha' :
                    print(' ')
                    print('Deu velha')
                    break
                else:
                    mostre_tabuleiro()
                    print(' ')
                    print('Você ganhou %s !' % nome_do_jogador)
                    break
    print('===================================================================')
    print(' ')
    jn = input('Deseja jogar novamente %s ? ' % nome_do_jogador) 
    print(' ')
    print('============================FIM DE JOGO============================')
            
            
        
        
            
        
    
    
    
    
    
            
            
            
            
            
            