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
    if ((tabuleiro[0][0]==tabuleiro[0][1]==tabuleiro[0][2]==('X' or 'O')) or 
    (tabuleiro[1][0]==tabuleiro[1][1]==tabuleiro[1][2]==('X' or 'O')) or 
    (tabuleiro[2][0]==tabuleiro[2][1]==tabuleiro[2][2]==('X' or 'O')) or
    (tabuleiro[0][0]==tabuleiro[1][0]==tabuleiro[2][0]==('X' or 'O')) or
    (tabuleiro[0][1]==tabuleiro[1][1]==tabuleiro[2][1]==('X' or 'O')) or
    (tabuleiro[0][2]==tabuleiro[1][2]==tabuleiro[2][2]==('X' or 'O')) or
    (tabuleiro[0][0]==tabuleiro[1][1]==tabuleiro[2][2]==('X' or 'O')) or
    (tabuleiro[0][2]==tabuleiro[1][1]==tabuleiro[2][0]==('X' or 'O'))) :
        print("O jogo terminou")