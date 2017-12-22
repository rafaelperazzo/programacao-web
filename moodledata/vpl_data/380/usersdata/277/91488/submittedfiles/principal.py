# -*- coding: utf-8 -*-
from minha_bib import *

while(True):
    n = ler_inteiro()
    mostrar_na_tela("%d! = %d" % (n,fatorial(n)))
    if not quer_continuar() :
        break