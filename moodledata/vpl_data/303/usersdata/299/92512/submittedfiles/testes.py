linha=[1,2,3]
tabuleiro=[linha]*3
simbolo=input('qual simbolo vc deseja usar?')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
jogada=str(input('qual sua jogada?'))
i=int(jogada[0])
j=int(jogada[1])
if i==0:
    if j==0:
        tabuleiro[0][0]=simbolo
    if j==1:
        tabuleiro[0][1]=simbolo
    if j==2:
        tabuleiro[0][2]=simbolo
if i==1:
    if j==0:
        tabuleiro[1][0]=simbolo
    if j==1:
        tabuleiro[1][1]=simbolo
    if j==2:
        tabuleiro[1][2]=simbolo
    else:
        print('erro de coordenada')
if i==2:
    if j==0:
        tabuleiro[2][0]=simbolo
    if j==1:
        tabuleiro[2][1]=simbolo
    if j==2:
        tabuleiro[2][2]=simbolo
    else:
        print('erro de coordenada')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
print(tabuleiro[i][j])