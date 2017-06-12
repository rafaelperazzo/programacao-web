# -*- coding: utf-8 -*-
n=int(input('digite o numero de pessoas:'))
tempoinicial=int(input('primeira passagem:'))
cont=0
for i in range(2,n,1):
    tempo=int(input('digite o tempo da passagem'))
    x=tempo-tempoinicial
    cont=cont+x
    tempoinicial=tempo
print(cont)    

            





