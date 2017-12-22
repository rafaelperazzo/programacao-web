linha=[0,1,2]
tabuleiro=[linha]*3
simbolo=input('qual simbolo vc deseja usar?')
jogada=str(input('qual sua jogada?'))
i=int(jogada[0])
j=int(jogada[1])

tabuleiro[i][j]=simbolo

a=tabuleiro[0][0]
b=tabuleiro[0][1]
c=tabuleiro[0][2]
d=tabuleiro[1][0]
e=tabuleiro[1][1]
f=tabuleiro[1][2]
g=tabuleiro[2][1]
h=tabuleiro[2][1]
i=tabuleiro[2][1]

print('',a,'|',b,'|',c,'\n',d,'|',e,'|',f,'\n',g,'|',h,'|',i)
