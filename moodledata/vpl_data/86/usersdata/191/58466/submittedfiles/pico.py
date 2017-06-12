# -*- coding: utf-8 -*-

def pico(b):
    for i in range(1,(len(b)//2)+1,1):
        if b[i]<b[i-1]:
            return False
        else:
            for i in range((len(b)//2)+1,len(b),1):
                if b[i]>b[i-1]:
                    return False
    return True 
    
n = input('Digite a quantidade de elementos da lista: ')
B=[]
for i in range(0,n,1):
    valor=float(input('digite o valor:'))
    B.append(valor)
if pico(B):
    print('S')
else:
    print('N')
