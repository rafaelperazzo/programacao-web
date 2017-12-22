# -*- coding: utf-8 -*-
g=int(input('Número de pedidos:'))
som=0
lista=[]
for i in range(g):
    b=int(input('Comprimento do taco:'))
    if b in lista:
        lista.remove(b)
    else:
        som+=2
        lista.append(b)
print(som)
