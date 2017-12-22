# -*- coding: utf-8 -*-
alturas = []

N = int(input())
while True:
    if 1 <= N <= 100000:
        break
    
    N = int(input())
    
for i in range(1, N+1):
    alt = int(input())
    while True:
        if 1 <= alt <= 1000000000:
            break
        
        alt = int(input())
    
    alturas.append(alt)
    
limite = min([alturas[0], alturas[len(alturas)-1]])

cont = 0

for i in alturas:
    if i < limite:
        cont += 1
    else:
        pass
    
print(cont)
    
