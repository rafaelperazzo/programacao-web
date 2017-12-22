linha=[0,1,2]
tabuleiro=[linha]*3
simbolo=input('qual simbolo vc deseja usar?')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
jogada=str(input('qual sua jogada?'))
i=int(jogada[0])
j=int(jogada[1])
if i==0 and j==0:
    tabuleiro[0][0]=simbolo
if i==0 and j==1:
    tabuleiro[0][1]=simbolo
if i==0 and j==2:
    tabuleiro[0][2]=simbolo
if i==1 and j==0:
    tabuleiro[1][0]=simbolo
if i==1 and j==1:
    tabuleiro[1][1]=simbolo
if i==1 and j==2:
    tabuleiro[1][2]=simbolo
if i==2 and j==0:
    tabuleiro[2][0]=simbolo
if i==2 and j==1:
    tabuleiro[2][1]=simbolo
if i==2 and j==2:
    tabuleiro[2][2]=simbolo
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
