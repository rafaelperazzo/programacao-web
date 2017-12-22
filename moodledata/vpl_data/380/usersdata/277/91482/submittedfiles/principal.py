# -*- coding: utf-8 -*-
from minha_bib import *

while(True):
    
    n = ler_inteiro()
    f = fatorial(n)
    mostrar_na_tela("%d! = %d" % (n,f))
    opt = input("Deseja continuar? [S ou N] ")
    if (opt == 'N') :
        mostrar_na_tela("\n\n ATE BREVE!")
        break