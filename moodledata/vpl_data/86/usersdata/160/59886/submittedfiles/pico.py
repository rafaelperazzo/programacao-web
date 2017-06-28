# -*- coding: utf-8 -*-

n=int(input('Digite a quantidade de elementos:'))
11=[]
for i in range (0,n,1):
    v=int(input('Digite os elementos da lista:'))
    11.append(v)
    
def pico(11):
    if 11[0]<11[1]:
        i=0
        cont=1
        while cont<n:
            if i==0:
                if 11[cont]<11[cont-1]:
                    i=1
                elif i==1:
                    if 11[cont]>11[cont-1]:
                        i=1
                else:
                    return False
                cont=cont+1
            return True
        else:
            return False

if pico(11):
    print('S')
else:
    print('N')
            