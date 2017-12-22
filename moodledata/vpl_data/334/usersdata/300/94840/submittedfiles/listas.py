# -*- coding: utf-8 -*-
m = int(input('Digite a quantidade de termos n: '))
n = []
for i in range(0,m,1):
    n.append(int(input('Digite um termo n: ')))
for i in range(1,m,1):
    h = 0
    p = n[i] - n[i-1]
    if p>0:
        p = p*(-1)
    while p > h:
        h = p
print(h)

           
        

#h = n[1] - n[0]
#if h<0:
#    h = h*(-1)
#for i in range(1,m,1):
#    ph = 0
#    p = n[i] - n[i-1]
#    while p<0:
#        p = p*(-1)
#    while p>h and p>ph:
#        ph = p
#hp = n[m-1] - n[m-2]
#if hp<0:
#    hp = hp*(-1)
#print(ph)
    
  
        

