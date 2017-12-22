# -*- coding: utf-8 -*-
from minha_bib import *

while(True):
    n = ler_inteiro()
    f = fatorial(n)
    mostrar_na_tela("%d! = %d" % (n,f))
    if not quer_continuar() :
        break
    
    