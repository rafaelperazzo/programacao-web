# -*- coding: utf-8 -*-
import math

def MDC(x, y):
    div_x = []
    div_y = []
    for i in range(1, x+1):
        if x%i == 0:
            div_x.append(i)
            
    for j in range(1, y+1):
        if y%j == 0:
            div_y.append(j)
    
    div_comum = div_x + div_y
    max_div_comum = max(div_comum)
    return max_div_comum
    
x = int(input("Digite um número inteiro positivo: "))
while True:
    if x>0:
        break
    x = int(input("Cara, eu falei POSITIVO! Digite novamente: "))

y = int(input("Digite outro inteiro positivo: "))
while True:
    if y>0:
        break
    y = int(input("Cara, eu falei POSITIVO! Digite novamente: "))
    
print(MDC(x, y))
