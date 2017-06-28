# -*- coding: utf-8 -*-

def picomax(x):
    for i in range(0,len(x)-1,1):
        if x[i]>x[i+1]:
            return (i)
            
def pico(x):
    a=picomax(x)
    for i in range (a,len(x)-1,1):
        if x[i]<x[i+1]:
            return false
    return false
    
    
n=int(input('escreva a quantidade de elementos:'))
a=[]
for i in range(0,n,1):
    d=int(input('digite o valor:'))
    a.append(d)
    
if pico(a):
        print('S')
else:
        print('N')
    #CONTINUE...
    


n = input('Digite a quantidade de elementos da lista: ')
#CONTINUE...
