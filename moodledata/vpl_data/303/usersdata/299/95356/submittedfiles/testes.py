tabela=[[[],[],[]],[[],[],[]],[[],[],[]]]
print('',tabela[0][0],'|',tabela[0][1],'|',tabela[0][2],'\n',tabela[1][0],'|',tabela[1][1],'|',tabela[1][2],'\n',tabela[2][0],'|',tabela[2][1],'|',tabela[2][2])
simbolo=input('qual simbolo vc deseja usar? ')
jogada=str(input('qual sua jogada? '))
simbolocpu='O'
i=int(jogada[0])
j=int(jogada[1])
print(i)
print(j)
tabela[i][j]=simbolo
print('',tabela[0][0],'|',tabela[0][1],'|',tabela[0][2],'\n',tabela[1][0],'|',tabela[1][1],'|',tabela[1][2],'\n',tabela[2][0],'|',tabela[2][1],'|',tabela[2][2])
#JOGADA DO COMPUTADOR
for i in range(0,3,1):
    for j in range(0,3,1):
        tabela[i][j]=simbolocpu