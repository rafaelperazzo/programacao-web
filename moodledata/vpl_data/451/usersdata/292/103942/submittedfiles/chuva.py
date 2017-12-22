# -*- coding: utf-8 -*-
N = int(input("Digite o número de seções da piscina: "))
while True:
    if 1 <= N <= 100000:
        break
    
    N = int(input("Número fora da faixa! Digite novamente: "))
    
