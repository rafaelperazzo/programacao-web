# -*- coding: utf-8 -*-
from minha_bib import *

while(True):
    while(True):
        n = int(input("Digite um numero inteiro positivo: "))
        if (n >= 0) :
            break
    f = fatorial(n)
    mostrar_na_tela("%d! = %d" % (n,f))
    opt = input("Deseja continuar? [S ou N] ")
    if (opt == 'N') :
        mostrar_na_tela("\n\n ATE BREVE!")
        break