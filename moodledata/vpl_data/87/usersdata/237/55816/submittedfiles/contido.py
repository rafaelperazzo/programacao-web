# -*- coding: utf-8 -*-
n=int(input("Digite n: "))
m=int(input("Digite m: "))
a=[]
for i in range(0,len(a),1):
    a.append(float(input("Digite o termo: ")))
b=[]
for i in range(0,len(b),1):
    b.append(float(input("Digite o termo: ")))
f=0    
for i in range(0,len(a),1):
    for u in range(0,len(b),1):
        if a[i] == b[u]:
            f=f+1
print(f)
    

