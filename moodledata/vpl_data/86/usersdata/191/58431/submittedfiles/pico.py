# -*- coding: utf-8 -*-

def pico(lista):
    for i in range(1,(len(lista)//2)+1,1):
        if lista[i]<lista[i-1]:
            return False
        else:
            for i in range((len(lista)//2)+1,len(lista),1):
                if lista[i]>lista[i-1]:
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
    print('N')_
