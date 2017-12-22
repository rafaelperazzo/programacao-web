# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
def tabuleiro():
    tab=[[],[],[]]
    while True:
        if (len(tab[0])+len(tab[1])+len(tab[2])<9:
            for i in range(0,2,1) :
                tab[0].append(str(input('simbolo: ')))
            for i in range(0,2,1) :
                tab[1].append(str(input('simbolo: ')))
            for i in range(0,2,1) :
                tab[2].append(str(input('simbolo: ')))
    print(tab[0][0]+ '|' + tab[0][1] + '|' + tab[0][2])
    print(tab[1][0]+ '|' + tab[1][1] + '|' + tab[1][2])
    print(tab[2][0]+ '|' + tab[2][1] + '|' + tab[2][2])

tabuleiro()

    

