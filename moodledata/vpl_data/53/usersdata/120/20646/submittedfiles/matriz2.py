# -*- coding: utf-8 -*-
from __future__ import division
#1passo:calcular o somatório das diagonáis principais
def somaDiagonal1(a):
    soma=0
    for i in range(0, a.shape[0],1):
        soma=soma+a[i,i]
    return soma

def somaDiagonal2(a):
    soma=0
    for i in range(0, a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
    return soma    






#2passo:calcular o somatório da diagonal secundária
#3passo:calcular os somatórios das colunas e das linhas
