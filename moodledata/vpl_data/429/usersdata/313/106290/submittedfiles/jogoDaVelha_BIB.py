class jogadainvalida(Exception):pass
def mostraTabuleiro(m):
    print """
    ----------------| %s | %s | %s |
    ----------------| %s | %s | %s |
    ----------------| %s | %s | %s |
    ----------------""" %(m[0][0],m[0][1],m[0][2],m[1][0],m[1][1],m[1][2],m[2][0],m[2][1],m[2][2])
    linha1=[' ',' ',' ']
    linha2=[' ',' ',' ']
    linha3=[' ',' ',' ']
    matriz=[linha1,linha2,linha3]
def joga(p):
    while 1:
        try:
            if p==1:x=(int(raw_input('Jogador 1 Escolha a linha a jogar')))-1y=(int(raw_input('Jogador 1 Escolha a coluna a jogar')))-1
            if matriz[x][y]==' ':matriz[x][y]='X'player=0breakelse:
                raise PositionErrorelse:x=int(raw_input('Jogador 2 Escolha a linha a jogar'))y=int(raw_input('Jogador 2 Escolha a coluna a jogar'))
                if matriz[x][y]==' ':matriz[x][y]='0'player=1breakelse:raise PositionErrorexcept IndexError:
                    print 'Valores fora do intervalo. Escolha entre 1 e 3 \n \n'except PositionError:
                        print 'Esta posicao ja foi jogada, por favor escolha outra \n \n'except ValueError:
                            print 'Introduza um valor inteiro entre 1 e 3!!! \n \n'
                            return player
def verifica(m,situacao):
flag=Falseif (m[0][0]==m[0][1]==m[0][2]=='X'):
    print 'Jogador 1 ganhou'situacao=Trueelif (m[1][0]==m[1][1]==m[1][2]=='X'):
        print 'Jogador 1 ganhou'situacao=Trueelif (m[2][0]==m[2][1]==m[2][2]=='X'):
            print 'Jogador 1 ganhou'situacao=Trueelif (m[0][0]==m[1][0]==m[2][0]=='X'):
                print 'Jogador 1 ganhou'situacao=Trueelif (m[0][1]==m[1][1]==m[2][1]=='X'):
                    print 'Jogador 1 ganhou'situacao=Trueelif (m[0][2]==m[1][2]==m[2][2]=='X'):
                        print 'Jogador 1 ganhou'situacao=Trueelif (m[0][0]==m[1][1]==m[2][2]=='X'):
                            print 'Jogador 1 ganhou'situacao=Trueelif (m[0][2]==m[1][1]==m[2][0]=='X'):
                                print 'Jogador 1 ganhou'situacao=Trueelif (m[0][0]==m[0][1]==m[0][2]=='0'):
                                    print 'Jogador 1 ganhou'situacao=Trueelif (m[1][0]==m[1][1]==m[1][2]=='0'):
                                        print 'Jogador 1 ganhou'situacao=Trueelif (m[2][0]==m[2][1]==m[2][2]=='0'):
                                            print 'Jogador 1 ganhou'situacao=Trueelif (m[0][0]==m[1][0]==m[2][0]=='0'):
                                                print 'Jogador 1 ganhou'situacao=Trueelif (m[0][1]==m[1][1]==m[2][1]=='0'):
                                                    print 'Jogador 1 ganhou'situacao=Trueelif (m[0][2]==m[1][2]==m[2][2]=='0'):
                                                        print 'Jogador 1 ganhou'situacao=Trueelif (m[0][0]==m[1][1]==m[2][2]=='0'):
                                                            print 'Jogador 1 ganhou'situacao=Trueelif (m[0][2]==m[1][1]==m[2][0]=='0'):
                                                                print 'Jogador 1 ganhou'situacao=Trueelse:for i in matriz:for j in i:
    if j==' ':
        flag=Trueif flag==False:
            print 'Empate'situacao=Truereturn situacao
def apaga():
    for i in range(0,25):
        print '\b'
player=1situacao=Falsewhile 1:apaga()desenha(matriz)player=joga(player)print playerdesenha(matriz)situacao=verifica(matriz,situacao)if situacao:raw_input('Pressione qualquer tecla para sair')break

