# -*- coding: utf-8 -*-

c=(int(input()))
tacos=[]
a=0
r=0
for i in range(0,c,1):
    tacos.append(int(input()))
i=0
while(True) :
    
 for j in range(0,c,1):
     if tacos[i]==tacos[j] :
         a=1
 i=i+1
 if a==0 :
     r=(int(r+2))
     
 if i==c :
     break

print(r)
































