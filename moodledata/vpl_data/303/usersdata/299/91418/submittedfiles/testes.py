#Velha
L[1][1]=00
L[1][2]=01
L[1][3]=02
L[2][1]=10
L[2][2]=11
L[2][3]=12
L[3][1]=20
L[3][2]=21
L[3][3]=22
from minha_bib import sorteio
print('---------------------------------------------------------')
print('Bem Vindo ao JodoDaVelha do grupo X(Nicholas, Eduardo, Sivini)')
nome=str(input('Qual seu nome(ou apelido)? '))
s=str(input('Qual simbolo você deseja utilizar no jogo? '))
print('Vencedor do sorteio para início do jogo: ',str(sorteio(1,1))
