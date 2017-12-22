# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('Digite o numero de elementos: '))
for z in range (0,n,1):
    a.append(input('Digite o A%d: '% (z+1)))
for w in range (0,n,1):
    a.append(input('Digite o A%d: '% (w+1)))

    
nleck = 0
def leck(conjunto):
    if conjunto [0] > conjunto[1]:
        nleck+=1
    for i in range (0,n,1):
        if (conjunto[i-1] < conjunto[i]) and (conjunto[i] > conjunto[i+1]):
            nleck+=1
    if conjunto[3]>conjunto[2]:
        nleck+=1
    if nleck==1:
        print ('S')
    else:
        print ('N')

