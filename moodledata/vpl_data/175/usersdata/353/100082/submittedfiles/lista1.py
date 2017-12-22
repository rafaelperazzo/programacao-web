# -*- coding: utf-8 -*-
n=int(input('valor de n:'))
np = 0
somap = 0
ni = 0
somai=0
for i in range (0,n): 
    o = []
    o.append(int(input('valor de n:')))
    
for i in range (0,n):
    if o[i] % 2==0:
        np = np + 1
        somap = somap + o[i]  
        
for i in range (0,n):
    if o[i] % 2==1:
        ni = ni + 1
        somai = somai + o[i]  

