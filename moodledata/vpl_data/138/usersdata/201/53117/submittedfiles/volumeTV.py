 -*- coding: utf-8 -*-
 V=int(input('Volume inicial:'))
 T=int(input('Variação do volume:'))
 soma=V
 for i in range(1,T+1,1):
     n=int(input('Muudança de volume:'))
     soma=soma+1
     if soma>100:
        soma=100
    elif soma<0:
        soma=0
print(soma)