
tabuleiro=[0,1,2]#,[0,1,2],[0,1,2]]
tabuleiro2=[0,1,2]
tabuleiro3=[0,1,2]
simbolo=input('qual simbolo vc deseja usar?')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
jogada=str(input('qual sua jogada?'))
i=jogada[0]
j=jogada[1]
if i==0:
    if j==0:
        tabuleiro[0]=simbolo
    elif j==1:
        tabuleiro[1]=simbolo
    else:
        tabuleiro[2]=simbolo
elif i==1:
    if j==0:
        tabuleiro2[0]=simbolo
    elif j==1:
        tabuleiro2[1]=simbolo
    else:
        tabuleiro2[2]=simbolo
else:
    if j==0:
        tabuleiro3[0]=simbolo
    elif j==1:
        tabuleiro3[1]=simbolo
    else:
        tabuleiro3[2]=simbolo
   
print('',tabuleiro[0],'|',tabuleiro[1],'|',tabuleiro[2],'\n',tabuleiro2[0],'|',tabuleiro2[1],'|',tabuleiro2[2],'\n',tabuleiro3[0],'|',tabuleiro3[1],'|',tabuleiro3[2])