# -*- coding: utf-8 -*-
from __future__ import division


'''
Dizemos que uma sequência com pelo menos 3 números inteiros e sem elementos consecutivos iguais é um pico, se tem um pedaço inicial crescente (estritamente) 
depois fica decrescente (estritamente) até o final. Escreva um programa que verifique se um conjunto é ou não um pico.
    - [1,2,1] é um pico, pois tem o pedaço inicial crescente [1,2] e depois decresce.
    - [1,5,3] é um pico, pois tem o pedaço inicial crescente [1,5] e depois decresce.
    - [2, 5, 10, 46, 25, 12, 7] é um pico, pois tem o pedaço inicial crescente [2, 5, 10, 46] e depois só decresce.
    - [13, 5, 4, 12, 3, 0, -3, -14] não é um pico, pois o seu pedaço inicial [13, 5] é decrescente.
    - [6, 7, 8, 9, 10] não é um pico, pois tem apenas um pedaço crescente.
    - [10, 9, 7, 4] não é um pico, pois tem apenas um pedaço decrescente.
    - [1, 2, 1, 2, 1, 2, 1] não é um pico, pois depois do pedaço inicial crescente [1, 2] não decresce até o final.

Utilize função(ões)

ENTRADA

- Quantidade de elementos da lista n

- Uma lista com n elementos

SAÍDA

'S' ou

'N'

EXEMPLOS

Seja a entrada n=3 e a lista [1,5,3], a saída deve ser:

'S'

Seja a entrada n=8 e a lista [13, 5, 4, 12, 3, 0, -3, -14], a saída deve ser:

'N'

'''

def pico(lista):
    #CONTINUE...
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
