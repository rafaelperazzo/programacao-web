# -*- coding: utf-8 -*-
import numpy as np    
n=int(input('digite a quant de linhas:'))
m=int(input('digite a quant de colunas:'))
a=np.zeros ((n,m))
c=int(input('digite a linha da torre:'))
d=int(input('digite a coluna da torre:'))
for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            a[i,j]=int(input('digite o valor:'))
linha=0
coluna=0
for i in range (0,a.shape[0],1):
    linha=linha+a[c,i]
for j in range (0,a.shape[1],1):
    coluna=coluna+a[i,d]
p=linha+coluna-2*a[c,d]
print (p)
    
    
    
            
        
        



    


