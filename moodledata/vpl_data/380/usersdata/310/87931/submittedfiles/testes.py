# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import random
print('Bem vindo ao JogoDaVelha do Grupo 1 [Caio,Hugo,Anderson,Juan]') 
a = input('Digite seu nome:')
b = input('Digite qual simbolo você quer usar, X ou O :  ')
while b!= 'X' and b!= 'O' and b!= 'x' and b!= 'o':
    b = input('Digite qual simbolo você quer usar, X ou O :  ')

começo =random.randint(0,1)
print (começo)
