# -*- coding: utf-8 -*-
import math

x= int(input('Digite um valor: '))
y= int(input('Digite um valor: '))
z= int(input('Digite um valor: '))
t= int(input('Digite um valor: '))

lista = (x, y, z, t)

def lecker (lista):
    
    if n==1:
        return N
    no_maximos = 0
    if lista(0) > lista(1):
        no_maximo +=1
    for i in range(1,n-1):
        if lista(i-1) < lista(i) and lista(i) < lista(i+1):
            no_maximo +=1
    if lista(n-1) > lista(n-2):
        no_maximo +=1
    return no_maximo ==1