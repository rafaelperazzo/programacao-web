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
    
#[2, 5, 10, 46, 25, 12, 7] -> SIM
#[2, 5, 10, 46, 25, 30] -> NAO

'''
1) Encontrar a posição do primeiro pico encontrado da sequência;
 0  1   2  3   4   5   6
[2, 5, 10, 46, 25, 12, 7]
Ex: posicaoPico = 3

2) A partir do índice do pico, verificar se o restante da lista é descrescente. 

'''


n = input('Digite a quantidade de elementos da lista: ')
a = []
for i in range(0,n,1):
    a.append(input('Digite um valor: '))


posicao = 0 
for i in range(0,len(a)-1,1):
    if a[i]>a[i+1]:
        posicao = i
        break

print posicao








