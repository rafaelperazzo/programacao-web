# -*- coding: utf-8 -*-
import itertools 
n=int(input('digíte a quantidade de números:'))
z=[]
for i in range(0,n,1):
    lista=int(input('digite o elemento desta lista:'))
    z.append(lista)
    
permut=list(itertools.permutations(z))

for i in range(0,n-1,1):
    p1=int(str(permut[i][0])+str(permut[i][1]))
    p2=int(str(permut[i][2])+str(permut[i][3]))
    
g=int(str(z[0])+str(z[1])+str(z[2])+str(z[3]))
print(g)

if p1*p2=g
    print('SIM, é vampiro')
else:
    print('Não é vampiro nem aqui e nem na china!!')
    

    
    
    
    
    
    
    
    

    