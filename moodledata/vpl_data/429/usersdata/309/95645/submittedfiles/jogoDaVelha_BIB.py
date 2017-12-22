# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI

def simb_humano():
    simbH= input("Olá humano,informe simbolo deseja utilizar para a partida: X ou O :  ")
    while simbH!="X" or simbH!="x" or simbH!="O" or simbH!="o"  :
        print ("Ops! Simbolo inválido")
        simbH= input("Informe um simbolo válido deseja utilizar para a partida: X ou O :  ")
    print ("Ok")

