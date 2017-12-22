# -*- coding: utf-8 -*-

m=(int(input()))
n=(int(input()))
quadras=[]
preco1=0
preco2=0
preco3=0
preco4=0
for i in range(0,m,1) :
    ruas=[]
    for j in range(0,n,1):
        ruas.append(int(input()))
    quadras.append(ruas)    
for i in range (0,m,1) :
    for j in range(0,n,1) :
        preco1=preco1+quadras[i][j]
        if j==0:
            preco1=0
        
        
        if  preco1<=preco2 and j==n-1 and preco1>0:
            preco2=preco1
            
        
for j in range (0,n,1):
  for i in range(0,m,1):
      preco3=preco3+quadras[i][j]
      
      if i==0 :
          preco3=0
      
      
      if  preco3<=preco4 and i==m-1 and preco3>0:
          preco4=preco3
      

if preco2<=preco4 :
     print(preco4)
else:
     print(preco2)











