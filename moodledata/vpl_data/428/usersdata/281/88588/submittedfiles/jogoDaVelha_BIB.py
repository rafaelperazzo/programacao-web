# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def simb ():
    simb= str(input('Qual o simbolo que voce quer ultilizar X ou O?'))
    while (simb != 'X' and simb != 'O'):
        print('Simbolo invalido')
        simb=str(input('Qual o simbolo que voce quer ultilizar X ou O?'))
        break
def cordenadavc ():
    x, y=input('Digite sua primeira coordenada no intervalo (0,2):').split(',')
    x, y= int(x), int(y)
    while int(x)!=0 or int(x)!=1 or int(x)!=2 and int(y)!=0 or int(y)!=1 or int(y)!=2:
        print('Coordenada invalida!')
        x, y=input('Digite sua primeira coordenada no intervalo (0,2):').split(',')
        x, y=int(x), int(y)
        break
    



    
        