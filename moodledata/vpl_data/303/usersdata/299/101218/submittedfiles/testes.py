from minha_bib import verificar_vitoria
from minha_bib import sorteio
from minha_bib import sorteio2
from minha_bib import maquinainteligente
from minha_bib import mostrar_tabuleiro
import time
tabuleiro=[[1,2,3],[1,2,3],[1,2,3]]
for i in range(0,3,1):
    for j in range(0,3,1):
        tabuleiro[i][j]=" "

print('---------------------------------------')
print('JOGO DA VELHA')
print('Olá\nSeja Bem Vindo ao jogo da velha!')

#JOGO ENTRE DUAS PESSOAS
nome1=str(input('Qual seu nome(ou apelido)? '))
'''nome2=str(input('Qual o nome do segundo jogador? '))'''
s1=str(input('Qual símbolo você deseja utilizar,'+nome1+'?[X/O]'))
if s1=='X':
    s2='O'
    '''print('Ok, vamos começar,'+nome2+' ficará com "O"')'''
    
else:
    s2='X'
    '''print('Ok, vamos começar,'+nome2+'ficará com "X"')'''
print('Esse é o nosso tabuleiro \n',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
print('Você vai me informar a casa que quer jogar com números.\n E cada um desses números representa as seguintes casas:')
print('00 | 01 | 02\n10 | 11 | 12\n20 | 21 | 22')
print('E aí eu vou lá e substituo a casa pelo seu símbolo, por exemplo:\nO você me informa a seguinte jogada: 22')
print('Eu vou lá e...')
print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',s2)
print('----------------------------------------------')
#COMEÇO DO JOGO
inicio=sorteio(0,1)
if inicio==0:
    inicio=str('Usuário')
else:
    inicio=str('Máquina')

print('O vencedor do sorteio para incio foi '+inicio)
if inicio=='Usuário':
    print('Então você começa')
    for k in range(1,10,1):
        if k%2!=0:
            jogada=str(input('Qual a sua jogada '+nome1+'?'))
            i=jogada[0]
            j=jogada[1]
            i=int(i)
            j=int(j)
            while tabuleiro[i][j]!=" ":
                print('Jogada inválida')
                jogada=str(input('Qual a sua jogada?'))
                i=jogada[0]
                j=jogada[1]
                i=int(i)
                j=int(j)
            tabuleiro[i][j]=s1
            print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
            if verificar_vitoria(tabuleiro)==True:
                print('PARABÉNS,VOCÊ VENCEU')
                break
            elif k==9 and verificar_vitoria(tabuleiro)==False:
                print('DEU VELHA!!!')
            else:
                continue
        elif k%2==0:
            print('Minha vez')
            time.sleep(2)
            x=str(maquinainteligente(tabuleiro))
            i=int(x[0])
            j=int(x[1])
            while tabuleiro[i][j]!=" ":
                x=str(maquinainteligente(tabuleiro))
                i=int(x[0])
                j=int(x[1])
            tabuleiro[i][j]=s2
            print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
            if verificar_vitoria(tabuleiro)==True:
                print('Ahh, não foi dessa vez')
                break
            elif k==9 and verificar_vitoria(tabuleiro)==False:
                print('DEU VELHA!!!')
            else:
                continue
elif inicio=='Máquina':
    print('Então eu começo')
    for k in range(1,10,1):
        if k%2!=0:
            print('Minha vez')
            time.sleep(2)
            x=str(maquinainteligente(tabuleiro))
            i=int(x[0])
            j=int(x[1])
            tabuleiro[i][j]=s2
            print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
            if verificar_vitoria(tabuleiro)==True:
                print('Ahh, não foi dessa vez')
                break
            elif k==9 and verificar_vitoria(tabuleiro)==False:
                print('DEU VELHA!!!')
            else:
                continue
        elif k%2==0:
            jogada=str(input('Qual a sua jogada '+nome1+'?'))
            i=jogada[0]
            j=jogada[1]
            i=int(i)
            j=int(j)
            while tabuleiro[i][j]!=" ":
                print('Jogada inválida')
                jogada=str(input('Qual a sua jogada?'))
                i=jogada[0]
                j=jogada[1]
                i=int(i)
                j=int(j)
            tabuleiro[i][j]=s1
            print('',tabuleiro[0][0],'|',tabuleiro[0][1],'|',tabuleiro[0][2],'\n',tabuleiro[1][0],'|',tabuleiro[1][1],'|',tabuleiro[1][2],'\n',tabuleiro[2][0],'|',tabuleiro[2][1],'|',tabuleiro[2][2])
            if verificar_vitoria(tabuleiro)==True:
                print('PARABÉNS,VOCÊ VENCEU')
                break
            elif k==9 and verificar_vitoria(tabuleiro)==False:
                print('DEU VELHA!!!')
            else:
                continue