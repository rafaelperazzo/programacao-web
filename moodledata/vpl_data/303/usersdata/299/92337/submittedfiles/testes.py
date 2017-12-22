linha=[0,1,2]
tabuleiro=[linha]*3
print(tabuleiro)
print(tabuleiro[0][0])
simbolo=input('qual simbolo vc deseja usar?')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
jogada=str(input('qual sua jogada?'))
i=jogada[0]
j=jogada[1]
tabuleiro[int(i)][int(j)]=simbolo
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
print(tabuleiro[0][0])