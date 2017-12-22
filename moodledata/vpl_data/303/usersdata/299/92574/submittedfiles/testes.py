from minha_bib import mostrar_tabuleiro
from minha_bib import sorteio
simbolo=input('qual simbolo vc deseja usar?')
primeiro=print('Vencedor do sorteio para início do jogo: '+sorteio(0,1))
jogada=str(input('qual sua jogada?'))
i=int(jogada[0])
j=int(jogada[1])
print(mostrar_tabuleiro(i,j,simbolo))
