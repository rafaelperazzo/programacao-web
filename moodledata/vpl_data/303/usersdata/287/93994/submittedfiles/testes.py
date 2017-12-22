# -*- coding: utf-8 -*-
from minha_bib import*
import time 
import os
import random
'''
board=[" "," "," "," "," "," "," "," "," "," "]
print(""+board[1]+"|"+board[2]+"|"+board[3]+"")
print(""+board[4]+"|"+board[5]+"|"+board[6]+"")
print(""+board[7]+"|"+board[8]+"|"+board[9]+"")
'''
'''
notas = []
for i in range(0,50,1):
    notas.append(float(input('digite a nota %d: ' % (i+1))))
media = 0
for i in range(0,50,1):
    media += notas[i]/5.0
print(notas)
print(media)
'''
'''
notas = []
for i in range(0,4,1):
    notas.append(float(input('digite a nota %d: ' % (i+1))))
media = 0
for i in range(0,50,1):
    media += notas[i]/4.0
print[1]
print(media)
'''
'''
n=[1,2,3,4,5,6]
print(n) #o vetor n
print(sum(n))
print(len(n))
del n[2]
print(n)
print(6 in n)
n.append(3)
print(n)
'''
'''
fatorial(5)
'''

'''
quadro([' ','O',' ',' ',' ',' ',' ',' ',' ',' '])

n=int(input('qual a sua jogada?'))
if n==11:
    quadro([' ','O',' ',' ','X',' ',' ',' ',' ',' '])
elif n==00:
        quadro(['X','O',' ',' ',' ',' ',' ',' ',' ',' '])
'''
'''
lista1=[7,5,9,4,0,2,32]
for i in range (0,len(lista1),1):
    print (lista1[i]//2)
    
'''
lista=[]
x=int(input('digite a quantidade de valores: '))
for i in range (0,x,1):
    lista.append(int(input('digite o valor do elemento%d:' % (i+1))))
soma=0
for i in range (0,x,1):
    soma+=lista[i]
    media=soma/x

termo1=1/(x-1) #PRIMEIRO TERMO DO DESVPAD
soma=0
for i in range(0,x,1):
    lista[i]-=1
    soma+=(lista[i]**2)
print(soma)
    

    













    
