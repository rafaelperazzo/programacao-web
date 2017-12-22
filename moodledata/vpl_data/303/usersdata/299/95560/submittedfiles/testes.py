
from minha_bib import sorteio

tabuleiro=[[1,1,1],[1,1,1],[1,1,1]]
for i in range(0,3,1):
    for j in range(0,3,1):
        tabuleiro[i][j]=str()

print('---------------------------------------')
print('JOGO DA VELHA')

print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
s2=0
#JOGO ENTRE DUAS PESSOAS
nome1=input('Qual o nome do primeiro jogador? ')
nome2=input('Qual o nome do segundo jogador? ')
s1=input('Qual símbolo você deseja utilizar, %d?[X/O] '%nome1)
if s1=='X':
    s2='O'
    print('Ok, vamos começar, %d ficará com "O"' %nome2)
    
elif s1=='O':
    s2='X'
    print('Ok, vamos começar, %d ficará com "X"'%nome2)
print('Esse é o nosso tabuleiro \n',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
print('Vocês vão me informar a casa que querem jogar com os números 00,01,02,10,11,12,20,21,22.\n E cada um desses números representa as seguintes casas:)
print(' 00 | 01 | 02\n10 | 11 | 12\n20 | 21 | 22')
print('E aí eu vou lá e substituo a casa pelo símbolo de vocês, por exemplo:\nO %d me informa a seguinte jogada: 22'%nome2)
print('Eu vou lá e...')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',s2)