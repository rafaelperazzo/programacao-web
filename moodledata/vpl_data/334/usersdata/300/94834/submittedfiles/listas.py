# -*- coding: utf-8 -*-
m = int(input('Digite a quantidade de termos n: '))
n = []
for i in range(0,m,1):
    n.append(int(input('Digite um termo n: ')))
h = n[1] - n[0]
if h<0:
    h = h*(-1)
for i in range(2,m+1,1):
    ph = 0
    p = n[i] - n[i-1]
    if p<0:
        p = p*(-1)
    if p>h and p>ph:
        ph = p
print(ph)            
        


    
  
        

