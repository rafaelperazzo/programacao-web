# -*- coding: utf-8 -*-
from datetime import datetime
import random 
# autenticação do simbolo para a jogada humano 

def simb_humano():
    simbH= input("Olá humano, informe o simbolo que deseja utilizar para a partida: X ou O :  ")
    while simbH!="X" and simbH!="x" and simbH!="O" and  simbH!="o"  :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido que deseja utilizar para a partida: X ou O :  ")
   
#sorteio
def sorteio ():
    now= datetime.now()
    a=now.minute
    if a%2==0:
        print("Quem inicia a partida, é você... Boa jogada")
    else:
        print("Quem inicia a partida, é máquina. Observe.")
        
        
        
        
# sorteio(Anderson)
def sorteio():
        
        
        
        

