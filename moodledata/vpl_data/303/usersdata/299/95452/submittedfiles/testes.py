
from minha_bib import sorteio
from minha_bib import analise_de_vencedor

x=0

tabela=[[1,1,1],[1,1,1],[1,1,1]]
simbolo=input('qual simbolo vc deseja usar jogador 1? ')
simbolocpu='O'

while x!='Venceu':
    jogada=str(input('qual sua jogada? '))
    i=int(jogada[0])
    j=int(jogada[1])
    tabela[i][j]=simbolo
    print('',tabela[0][0],'|',tabela[0][1],'|',tabela[0][2],'\n',tabela[1][0],'|',tabela[1][1],'|',tabela[1][2],'\n',tabela[2][0],'|',tabela[2][1],'|',tabela[2][2])
    x=analise_de_vencedor(tabela)
    
    jogada=str(input('qual sua jogada, jogador 2? '))
    i=int(jogada[0])
    j=int(jogada[1])
    tabela[i][j]=simbolocpu
    print('',tabela[0][0],'|',tabela[0][1],'|',tabela[0][2],'\n',tabela[1][0],'|',tabela[1][1],'|',tabela[1][2],'\n',tabela[2][0],'|',tabela[2][1],'|',tabela[2][2])
    x=analise_de_vencedor(tabela)