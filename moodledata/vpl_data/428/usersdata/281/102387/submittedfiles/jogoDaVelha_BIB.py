# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def simb ():
    simb= str(input('Qual o simbolo que voce quer ultilizar X ou O?'))
    while (simb != 'X' and simb != 'O'):
        print('Simbolo invalido')
        simb=str(input('Qual o simbolo que voce quer ultilizar X ou O?'))

def sorteio ():
    sort=random.choice((1,0))
if sort==1:
    print('Vencedor do sorteio para inicio do jogo:' +nome)
    
    
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    n=random.choice(('00','01','02','10','11','12','20',21,'22')) #sorteio das posiçoes no quadro
    n=print(n)





def mostratabuleiro(board):
    print(board[0],'|',board[1],'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])
        


    



    
        