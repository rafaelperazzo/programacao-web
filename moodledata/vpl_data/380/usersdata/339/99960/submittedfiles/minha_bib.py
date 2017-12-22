# -*- coding: utf-8 -*-

def tabuleiro():
    tab=[[],[],[]]
    for i in range(0,3,1) :
        tab[0].append(str(input('simbolo tab0: ')))
    for i in range(0,3,1) :
        tab[1].append(str(input('simbolo tab1: ')))
    for i in range(0,3,1) :
        tab[2].append(str(input('simbolo tab2: ')))
    print(tab[0][0]+ '|' + tab[0][1] + '|' + tab[0][2])
    print(tab[1][0]+ '|' + tab[1][1] + '|' + tab[1][2])
    print(tab[2][0]+ '|' + tab[2][1] + '|' + tab[2][2])
        
def vencedor():
    tabuleiro()
    if str(tab[0][0])==str(tab[0][2]) and str(tab[0][0])==str(tab[0][1]) and str(tab[0][1])==str(tab[0][2]):
        print (tab[0][0])
    elif tab[1][0]==tab[1][1] and tab[1][1]==tab[1][2] and tab[1][0]==tab[1][2]:
        print (tab[1][0])
    elif tab[2][0]==tab[2][1] and tab[2][1]==tab[2][2] and tab[2][0]==tab[2][2]:
        print (tab[2][0])
    else:
        print ('velha')
    return
        
        




