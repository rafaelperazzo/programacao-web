# -*- coding: utf-8 -*-
n=int(input("Insira n: "))
while not(1 <= n <= 10**5):
    n=int(input("Insira n: "))
pool=[]
h=0
for i in range (0,n,1):
    h=(int(input("Insira um h: ")))
    while h < 1 or h > 10**9:
        h=(int(input("Insira um h: ")))
    pool.append(h)
    
lim=0

if pool[0] <= pool[n-1]:
    lim=pool[0]
if pool[0] > pool[n-1]:
    lim=pool[n-1]

cont=0
for i in range (0,n,1):
    if pool[i]<lim:
        cont=cont+1
        
print(cont)



    
    
    