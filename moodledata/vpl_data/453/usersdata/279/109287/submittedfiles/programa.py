# -*- coding: utf-8 -*-
n=(int(input()))
a=0
soma1=0
soma2=0
posicoes=[]
for i in range(0,n,1):
    linhas=[]
    for j in range(0,n,1) :
        linhas.append(int(input()))
    posicoes.append(linhas)    
i=0
somal=[]
somac=[]
while(True) :
    
   
   for j in range(0,n,1) :
    soma1=(soma1+posicoes[i][j])
    soma2=(soma2+posicoes[j][i])
   somal.append(soma1)
   somac.append(soma2)
   i=i+1
   if (i==n) :
       break
       
for i in range(0,n,1) :
    for j in range(0,n,1) :
        if ((somal+somac-posicoes[i][j])>=a) :
            a=(somal+somac-posicoes[i][j])
        
            
print(a)










































