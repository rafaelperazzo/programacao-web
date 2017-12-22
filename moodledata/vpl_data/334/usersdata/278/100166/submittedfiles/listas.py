# -*- coding: utf-8 -*-
n = int(input("Digite a quantidade de termos da lista x: "))
x = []
for i in range (0,n,1):
    x.append(int(input("Digite o elemento%.d da lista x: " %(i+1))))
b=0
if i<(n-1):
    altura_b = x[i]-x[i+1]
for i in range (0,n,1):
        if altura_b<0:
            altura_b*=-1
        b+=1
c=0
for y in range (0,b,1):
    for z in range (y,b,1):
        if altura_y>altura_z:
            c+=1
        else:
            c*=0
if c>0:
    print(c)
            
        

