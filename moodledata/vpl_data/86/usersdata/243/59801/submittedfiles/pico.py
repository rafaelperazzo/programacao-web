# -*- coding: utf-8 -*-

n=int(input('digite a quantidade de elementos da lista:'))
l1=[]
for i in range(0,n,1):
    v=int(input('digite o elementos da lista:'))
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
                retun False
            cont=cont+1
        return True
    else:
        return False
        
if pico(l1):
    print('S')
else:
    print('N')