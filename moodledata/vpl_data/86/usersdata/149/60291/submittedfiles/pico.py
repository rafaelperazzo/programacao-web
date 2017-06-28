# -*- coding: utf-8 -*-

def max(n):
   
    for i in range(0,len(n)-1,1):
        if n[i]>n[i+1]:
            return(i)
        
def pico(b):
    m=pmax(b)
    for j in range (m,len(b)-1,1):
        if b[j]<b[j+1]:
            return(False)
    return(True)
        
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(0,n,1):
    valor=float(input('digite O elementos da lista:'))
    a.append(valor)
    
if (pico(a)):
    print('S')
else:
    print('N')

