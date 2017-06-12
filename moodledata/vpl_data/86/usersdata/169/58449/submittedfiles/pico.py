# -*- coding: utf-8 -*-
n=int(input('Digite a Quantidade de Elementos da Lista:'))
l1=[]
for i in range(0,n,1):
    v=int(input('Digite os Elementos da Lista:'))
    l1.append(v)
    
def pico(l1):
    if l1[0]<l1[1]:
        i=0
        cont=1
        while cont<n:
            if i==0:
                if l1[cont]<l1[cont-1]:
                    i=1
            elif i==1:
                if l1[cont]>l1[cont-1]:
                    i=2
            else:
                return False
            cont=cont+1
        return True
    else: 
        return False
        

if pico(l1):
    print('S')
else:
    print('N')
    
    
