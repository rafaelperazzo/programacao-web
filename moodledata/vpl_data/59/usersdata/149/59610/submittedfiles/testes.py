# -*- coding: utf-8 -*-
import itertools 
n=4
z=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento desta lista:'))
    z.append(lista)
g=int(str(z[0])+str(z[1])+str(z[2])+str(z[3]))
permut=list(itertools.permutations(z))
print(permut)
cont=0
for i in range(0,23,1):
    p=int(str(permut[i][0])+str(permut[i][1]))*int(str(permut[i][2])+str(permut[i][3]))
    if p==g:
        cont=cont+1
if cont>=1:
    print('S')
else:
    print('N')


    

    
    
    
    
    
    
    
    

    