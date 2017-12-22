
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
nome1=str(input('Qual o nome do primeiro jogador? '))
nome2=str(input('Qual o nome do segundo jogador? '))
s1=str(input('Qual símbolo você deseja utilizar,'+nome1+'?[X/O]'))
if s1=='X':
    s2='O'
    print('Ok, vamos começar,'+nome2+' ficará com "O"')
    
elif s1=='O':
    s2='X'
    print('Ok, vamos começar,'+nome2+'ficará com "X"')
print('Esse é o nosso tabuleiro \n',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
print('Vocês vão me informar a casa que querem jogar com números.\n E cada um desses números representa as seguintes casas:')
print('00 | 01 | 02\n10 | 11 | 12\n20 | 21 | 22')
print('E aí eu vou lá e substituo a casa pelo símbolo de vocês, por exemplo:\nO',nome2,' me informa a seguinte jogada: 22')
print('Eu vou lá e...')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',s2)