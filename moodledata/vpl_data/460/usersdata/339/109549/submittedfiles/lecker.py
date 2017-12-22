# -*- coding: utf-8 -*-
import math

def lecker(x,y):
    som1=0
    for i in range(1,len(x)+1):
        if x[i]>x[i+1] and x[i]>x[i-1]:
            som1+=1
        elif x[i]==x[i+1] and x[i]==x[i-1]:
            som1+=1
    if som1==1:
        print('S')
    else:
        print('N')
    som2=0
    for i in range(1,len(y)+1):
        if y[i]>y[i+1] and y[i]>y[i-1]:
            som2+=1
        elif y[i]==y[i+1] and y[i]==y[i-1]:
            som2+=1
    if som2==1:
        print('S')
    else:
        print('N')
    return

n=int(input('Quantidade de elementos:'))
a=[]
b=[]

for j in range(n):
    a.append(float(input('elementos a:')))
for j in range(n):
    b.append(float(input('elementos b:')))
    
lecker(a,b)





            
        
        