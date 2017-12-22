# -*- coding: utf-8 -*-
def analiseintersec(x,y):

listan=[]
listam=[]
n=int(input(''))
m=int(input(''))

for i in range(0,n,1):
    listan.append(int(input('')))
for i in range(0,m,1):
    listam.append(int(input('')))
    
    
cont+=1
for i in range(0,n,1):
    for j in range(0,m,1):
        if listan[i]==listam[j]:
            cont+=1
        else:
            cont+=0
print(cont)



