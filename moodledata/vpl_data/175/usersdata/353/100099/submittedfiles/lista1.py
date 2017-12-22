# -*- coding: utf-8 -*-
n=int(input('valor de n:'))
np = 0
somap = 0
ni = 0
o = []
somai=0

for i in range (0,n,1): 
    o.append(int(input()))
    
for i in range (0,n,1):
    if o[i] % 2==0:
        np = np + 1
        somap = somap + o[i]  
        
for i in range (0,n,1):
    if o[i] % 2==1:
        ni = ni + 1
        somai = somai + o[i]  

print (ni)
print(np)
print(somai)
print(somap)