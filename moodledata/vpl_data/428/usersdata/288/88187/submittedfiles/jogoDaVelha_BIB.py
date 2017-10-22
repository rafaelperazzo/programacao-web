# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def simbolo ():
    simbolo=str(input("Escolha um simbolo [X ou O]: "))
    while (simbolo!='X' and simbolo!='O'):
            print ("SIMBOLO INVALIDO!")
            simbolo=str(input("Escolha um simbolo [X ou O]: "))
    print ("pronto")
def sort ():
    sort=random.randint(1,2)