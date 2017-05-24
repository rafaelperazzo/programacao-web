# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
import math
#bin=int(input('Digite um texto: '))
#i=0
#soma=0
#while bin>0:
#    m=bin%10
#    soma=soma+m*2**i
#    bin=bin//10
#    i=i+1
#print(soma)    
#
#dec=int(input('Digite um número da base decimal: '))
#binario=bin(dec)
#print(binario[2:])
#a=10
#b=math.factorial(a)
#bin=int(input('Digite um texto: '))
#soma=0
#i=0
#while bin>0:
#    m=bin%10
#    soma=soma+m*2**i
#    bin=bin//10
#    i=i+1
#print(soma)    
#
#Sub-número
#p=int(input('Digite um texto: '))
#q=int(input('Digite um texto: '))
#i=len(str(p))
#cont=0
#while q>0:
#    resto=q%(10**i)
#    if resto==p:
#        cont=cont+1
#    q=q//10
#if cont!=0:
#    print('s')
#else:
#    print('n')
#
a=int(input('Digite um texto: '))
b=int(input('Digite um texto: '))
c=int(input('Digite um texto: '))
i=0
cont=0
while cont==0:
    nvalor=c-(a*i)
    if nvalor%b==0:
        print(i)
        print(nvalor/b)
        cont=1
    if (a*i)>c:
        print("n")
        cont=1
    i=i+1











