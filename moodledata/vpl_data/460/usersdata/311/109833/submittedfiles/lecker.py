# -*- coding: utf-8 -*-
a=[]
b=[]
n=int(input('Digite o numero de elementos: '))
while n<=2:
    n=int(input('Digite o numero de elementos: '))
for z in range (0,n,1):
    a.append(input('Digite o A%d: '% (z+1)))
for w in range (0,n,1):
    b.append(input('Digite o A%d: '% (w+1)))

    

#Função que vai me falar se é lecker
def leck(lec):
    nleck = 0
    if lec[0] >lec[1]:
        nleck+=1
    if lec[len(lec)-1] > lec[len(lec)-2]:
        nleck+=1
    for i in range (0,n-2,1):
        if lec[i]<lec[i+1] and lec[i+1]>lec[i+2]:
            nleck+=1
    if nleck==1:
        return True
    else: 
        return False

if leck(a):
    print ('S')
else:
    print ('N')
if leck(b):
    print ('S')
else:
    print ('N')


