# -*- coding: utf-8 -*-
import itertools 
n=int(input('digíte a quantidade de números:'))
z=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento desta lista:'))
    z.append(lista)

g=int(str(z[0])+str(z[1])+str(z[2])+str(z[3]))
    
permut=list(itertools.permutations(z))
print(permut)

for i in range(0,n,1):
    p1=int(str(permut[i][0])+str(permut[i][1]))
    p2=int(str(permut[i][2])+str(permut[i][3]))
    

p3=permut[1]
print(p3)

p4=permut[3]
print(p4)
    

    
    
    
    
    
    
    
    

    