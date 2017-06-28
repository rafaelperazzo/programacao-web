# -*- coding: utf-8 -*-
def maiordegrau(a):
    maior=0
    for i in range(0,len(a)-1,1):
        h=a[i]-a[i+1]
        if h>maior:
            maior=h
    Return maior
lista=[]
n=int(input('Digite o tamnaho da lista:'))
for i in range(0,i,1):
    a=int(input('Digite um valor para a lista:'))
maiordegrau(lista)

