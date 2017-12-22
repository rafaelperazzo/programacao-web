linha=[0,1,2]
tabuleiro=[linha]*3
print(tabuleiro)
print(tabuleiro[0][0])
simbolo=input('qual simbolo vc deseja usar?')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
jogada=int(input('qual sua jogada?'))
if 00 in jogada:
    tabuleiro[0][0]=simbolo
if 01 in jogada:
    tabuleiro[0][1]=simbolo
if 02 in jogada:
    tabuleiro[0][2]=simbolo
if 10 in jogada:
    tabuleiro[1][0]=simbolo
if 11 in jogada:
    tabuleiro[1][1]=simbolo
if 12 in jogada:
    tabuleiro[1][2]=simbolo
if 20 in jogada:
    tabuleiro[2][0]=simbolo
if 21 in jogada:
    tabuleiro[2][1]=simbolo
if 22 in jogada:
    tabuleiro[2][2]=simbolo
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
