# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def sorteio(x,y):
    import random 
    sort=random.randint(0,1)
    if sort==1:
        return(0)
    else:
        return(1)

def sorteio2(x,y):
    import random 
    sort=random.randint(0,2)
    return(sort)

tabela=[[0,1,2],[0,1,2],[0,1,2]]
print('',tabela[0][0],'|',tabela[0][1],'|',tabela[0][2],'\n',tabela[1][0],'|',tabela[1][1],'|',tabela[1][2],'\n',tabela[2][0],'|',tabela[2][1],'|',tabela[2][2])
simbolo=input('qual simbolo vc deseja usar? ')
jogada=str(input('qual sua jogada? '))
i=int(jogada[0])
j=int(jogada[1])
print(i)
print(j)
tabela[i][j]=simbolo
print('',tabela[0][0],'|',tabela[0][1],'|',tabela[0][2],'\n',tabela[1][0],'|',tabela[1][1],'|',tabela[1][2],'\n',tabela[2][0],'|',tabela[2][1],'|',tabela[2][2])