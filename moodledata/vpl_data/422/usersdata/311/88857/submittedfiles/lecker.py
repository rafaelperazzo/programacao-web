# -*- coding: utf-8 -*-
import math
l1=int(input('Digite um numero: '))
l2=int(input('Digite um numero: '))
l3=int(input('Digite um numero: '))
l4=int(input('Digite um numero: '))
conjunto=[l1,l2,l3,l4]
def lecker(conjunto):
    n=len(conjunto)
    if n==1:
        return false
    #quantidade de numeros maiores que seus vizinhos
    numerosleck=0
    if conjunto [0] > conjunto[1]:
        numerosleck += 1
    for i in range (1,3):
        if (conjunto[i-1] < conjunto[i]) and (conjunto[i] > conjunto[i+1]):
            numerosleck+=1
    if conjunto[3]>conjunto[2]:
        numerosleck+=1
    return numerosleck==1
if numerosleck==1:
    print ('S')
else:
    print ('N')

