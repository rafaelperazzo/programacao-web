# -*- coding: utf-8 -*-
v = int(input("Digite o volume inicial da televisão: "))
k, vol_f = [v], 0
del v
t = int(input("Digite o número de trocas de volume: "))

for i in range(1, t+1):
    k.append(int(input("Digite a %dº modificação: "%i)))
    
del t
for i in range(0, len(k)):
    vol_f += k[i]
    if vol_f > 100:
        vol_f = 100
        
    if vol_f < 0:
        vol_f = 0

print(vol_f)