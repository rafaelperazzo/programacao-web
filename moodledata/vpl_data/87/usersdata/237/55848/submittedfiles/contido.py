# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
m=int(input("Digite m: "))
a=[]
for i in range(0,n,1):
    a.append(float(input("Digite o termo: ")))
b=[]
for i in range(0,m,1):
    b.append(float(input("Digite o termo: ")))
f=0    
for i in range(0,len(a),1):
    for u in range(0,len(b),1):
        print (a[i],b[u])
            

    

