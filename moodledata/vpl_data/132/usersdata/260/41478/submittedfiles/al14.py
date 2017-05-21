# -*- coding: utf-8 -*-
n=int(input("digite o número de pessoas:"))
altura=0
total=0
media=0
for i in range (1,n+1,1):
    alturas=int(input("digite a altura dessas pessoa "+str(i)+(":")))
    total=alturas+total
media=total//n
print(media)
    