
from minha_bib import sorteio

tabuleiro=[[1,1,1],[1,1,1],[1,1,1]]
for i in range(0,3,1):
    for j in range(0,3,1):
        tabuleiro[i][j]=str()

print('---------------------------------------')
print('JOGO DA VELHA')

print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2],)

