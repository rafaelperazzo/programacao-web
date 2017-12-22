# -*- coding: utf-8 -*-
alturas = []

N = int(input("Digite o número de seções da piscina: "))
while True:
    if 1 <= N <= 100000:
        break
    
    N = int(input("Número fora da faixa! Digite novamente: "))
    
for i in range(1, N+1):
    alturas.append(int(input("Digite a altura da %dº seção: "%i)))
    
