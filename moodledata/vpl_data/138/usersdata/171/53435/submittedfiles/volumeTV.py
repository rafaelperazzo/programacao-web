 -*- coding: utf-8 -*-
 vi=int(input('digite o volume inicial:'))
 n=int(input('digite o numero de troca de volume:'))
 soma=0
 for i in range(1,n+1,1):
     x=int(input('digite o numero de vezes que o botao foi pressionado:'))
     if soma >=0 and soma<=100:
         soma=soma+x
print(soma)