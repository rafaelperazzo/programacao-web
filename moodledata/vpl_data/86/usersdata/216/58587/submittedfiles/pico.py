# -*- coding: utf-8 -*-




def pico(x):
    for i in range(0,len(x)-1,1):
        unico=0
        temp =0
        if unico==0:
            if x[i]<x[1]:
                return True
            else:
                return False
                break
                unico=unico+1
        else:
            if x[i]>x[i+1]:
                return True
            else:
                return False
                break

n = int(input('Digite a quantidade de elementos da lista: '))
a=[]
for i in range(0,n,1):
    d=int(input('Digite o valor:'))
    a.append(d)
    
if pico(a):
    print('S')
else:
    print('N')