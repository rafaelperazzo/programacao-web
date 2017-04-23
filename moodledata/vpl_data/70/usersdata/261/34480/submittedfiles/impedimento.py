# -*- coding: utf-8 -*-
import math
#COMECE SEU CÓDIGO AQUI
def impedimento():
    l = int(input("Qual a posição do jogador atacante que lança a bola? "))
    r = int(input("Qual a posição do jogador atacante que recebe a bola? "))
    d = int(input("Qual a posição do último jogador defensor? "))
    
    if R>50 and L<R and R>D:
        print ("S")
    else:
        print ("N")
        
impedimento()