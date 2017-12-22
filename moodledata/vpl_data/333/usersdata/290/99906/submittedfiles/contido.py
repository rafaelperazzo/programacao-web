# -*- coding: utf-8 -*-
def contido(c,d):
    f=0
    for i in range(0,len(d),1):
        if d[i] in c:
          f+=1
    return f
a=[]
b=[]
n=int(input("Digite a quantidades de elementos de a: "))
m=int(input("Digite a quantidades de elementos de b: "))
for i in range(0,n,1):
    a.append(int(input("Digite um elemento de a: ")))
for i in range(0,m,1):
    b.append(int(input("Digite um elemento de b: ")))
print(contido(a,b))
        

    
    

