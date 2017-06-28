# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um numero de 4 digitios:'))
lista=[]
#Usaremos outra variável, pois o valor de "n" será usado posteriormente.
z=n
#Criaremos uma repetição para anexar os valores dos dígitos de "n" em uma lista, para facilitar o seu acesso.
while z>0:
    valor=z%10
    z=z//10
    lista.insert(0,valor)
#Definimos uma função para saber se o número é ou não vampiro.
def vampiro(lista):
    if ((lista[0]*10)+lista[1])*((lista[2]*10)+lista[3])==n:
        return True
    elif ((lista[0]*10)+lista[1])*((lista[3]*10)+lista[2])==n:
        return True
    elif ((lista[1]*10)+lista[0])*((lista[2]*10)+lista[3])==n:
        return True
    elif ((lista[1]*10)+lista[0])*((lista[3]*10)+lista[2])==n:
        return True
    elif ((lista[0]*10)+lista[2])*((lista[1]*10)+lista[3])==n:
        return True
    elif ((lista[0]*10)+lista[2])*((lista[3]*10)+lista[1])==n:
        return True
    elif ((lista[2]*10)+lista[0])*((lista[1]*10)+lista[3])==n:
        return True
    elif ((lista[2]*10)+lista[0])*((lista[3]*10)+lista[1])==n:
        return True
    elif ((lista[0]*10)+lista[3])*((lista[1]*10)+lista[2])==n:
        return True
    elif ((lista[0]*10)+lista[3])*((lista[2]*10)+lista[1])==n:
        return True
    elif ((lista[3]*10)+lista[0])*((lista[1]*10)+lista[2])==n:
        return True
    elif ((lista[3]*10)+lista[0])*((lista[2]*10)+lista[1])==n:
        return True
    else:
        return False
if vampiro(lista)==True:
    print('o numero testado é vampiro')
