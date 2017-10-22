# -*- coding: utf-8 -*-

# COLOQUE SUA BIBLIOTECA A PARTIR DAQUI
def simbolo ():
    simbolo=str(input("Escolha um simbolo [X ou O]: "))
    while (simbolo!='X' and simbolo!='O'):
            print ("SIMBOLO INVALIDO!")
            simbolo=str(input("Escolha um simbolo [X ou O]: "))
    print ("pronto")
def random ():
    random=(2**3)*13
    if random%2==0:
        print("1")
    else:
        print('2')