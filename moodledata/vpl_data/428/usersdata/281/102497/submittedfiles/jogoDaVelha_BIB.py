# -*- coding: utf-8 -*-
# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
jogo_da_velha=[]

def simb ():
    nome=str(input('Qual o seu nome (ou apelido)? '))
    simb= str(input('Qual o simbolo que voce quer ultilizar X ou O? '))
    while (simb != 'X' and simb != 'O'):
        print('Simbolo invalido')
        simb=str(input('Qual o simbolo que voce quer ultilizar X ou O? '))

def sorteio ():
    sort=random.choice((1,0))
if sort==1:
    print('Vencedor do sorteio para inicio do jogo: ' +nome)
else:
    print('Vencedor do sorteio para inicio do jogo: Computador')
    

    
