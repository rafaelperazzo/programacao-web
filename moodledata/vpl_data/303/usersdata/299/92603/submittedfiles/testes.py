from minha_bib import mostrar_tabuleiro
from minha_bib import sorteio
simbolo2=0
simbolo=input('qual simbolo vc deseja usar?')
if simbolo=='X' or simbolo=='x':
    simbolo2=='O'
else:
    simbolo2=='X'
    
if sorteio(0,1)==0:
    primeiro='Computador'
else:
    primeiro='Usuário'
    
print('Vencedor do sorteio para início do jogo: '+primeiro)
if primeiro=='Computador':
    i=sorteio2(0,2)
    j=sorteio2(0,2)
    print(mostrar_tabuleiro(i,j,simbolo2))

jogada=str(input('qual sua jogada?'))
i=int(jogada[0])
j=int(jogada[1])
print(mostrar_tabuleiro(i,j,simbolo))
