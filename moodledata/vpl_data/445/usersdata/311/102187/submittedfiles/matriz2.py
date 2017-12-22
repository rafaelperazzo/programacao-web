# -*- coding: utf-8 -*-
import numpy
#função que verifica a magia da matriz
def magimatriz(matriz):
    for i in range (0,(len(a)-1),1):
        if sum(matriz[0])==sum(matriz[1]):
            return 'S'
    
        
n=int(input('Digite a dimensão da matriz: '))
while n<2:
    n=int(input('Digite a dimensão da matriz: '))
a=numpy.empty([n,n])
for w in range (0,n,1):
    for j in range (0,n,1):
        a[w] [j]=float(input('Digite o A%d%d: ' % ((w+1),(j+1))))
print (magimatriz(a))
print (a)
        

    
        
        
        
        
        
        
        
        
        
        
        


