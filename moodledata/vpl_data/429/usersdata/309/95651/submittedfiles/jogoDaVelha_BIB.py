# -*- coding: utf-8 -*-
from datetime import datetime
# autenticação do simbolo ao jogador humano 

def simb_humano():
    simbH= input("Olá humano,informe simbolo deseja utilizar para a partida: X ou O :  ")
    while simbH!="X" and simbH!="x" and simbH!="O" and  simbH!="o"  :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido que deseja utilizar para a partida: X ou O :  ")
   
def sorteio ():
    a=now.second
    if a%2==0:
        print("Quem inicia a partida, é você... Boa jogada")
    else:
        print("Quem inicia a partida, é máquina.Observe.")
        

