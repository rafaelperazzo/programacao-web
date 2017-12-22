# -*- coding: utf-8 -*-
piscina=[]
n=int(input(''))
for i in range(0,n,1):
    piscina.append(int(input('')))
#deterinando maior borda
borda=0
for i in range(0,n,1):
    for k in range(n-1,-1,-1):
        if piscina[i]==piscina[k]:
            borda=piscina[k]
        else:
            continue
cont=0
for i in range(0,n,1):
    if piscina[i]<borda:
        cont+=1
    else:
        continue
print(cont)
    
