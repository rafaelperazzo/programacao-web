# -*- coding: utf-8 -*-

n=(int(input()))
m=(int(input()))
matriz=[]
a=-1
for i in range(0,n,1) :
  vetor=[]
  
 for j in range(0,m,1) :
    vetor.append(int(input()))
 matriz.apppend(vetor)
for i in range(0,n,1) :
    for j in range(0,m,1) :
           if matriz[i][j]==0:
               a=a+1
               if j=m-1 and a=j+1 :
                  del matriz [i]
                  a=0
                  break
          
for i in range(0,n,1) :
    for j in range(0,m,1) :
           if matriz[i][j]==0:
               a=a+1
               if j=m-1 and a=j+1 :
                  del matriz [i]
                  a=0
                  break








