# -*- coding: utf-8 -*-
import numpy
#função que verifica a magia da matriz
def magimatriz(matriz):
    for i in range (0,(len(matriz)-1),1):
            if sum(matriz[i])==sum(matriz[i+1]):
                if matriz[i][0]+matriz[i+1][0]==matriz[i][1]+matriz[i+1][1]:
                return 'S'
            else:
                return 'N'
    
        
n=int(input('Digite a dimensão da matriz: '))
while n<2:
    n=int(input('Digite a dimensão da matriz: '))
a=numpy.empty([n,n])
for w in range (0,n,1):
    for j in range (0,n,1):
        a[w] [j]=float(input('Digite o A%d%d: ' % ((w+1),(j+1))))
print (magimatriz(a))
print (a)
        

    
        
        
        
        
        
        
        
        
        
        
        


