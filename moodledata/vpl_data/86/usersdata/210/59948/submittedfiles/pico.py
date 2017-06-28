# -*- coding: utf-8

def picomax(x):
    for i in range(0,len(x)-1,1):
        if x[i]>x[i+1]:
            return (i)
            
def pico(x):
    a=picomax(x)
    for i in range (a,len(x)-1,1):
        if x[i]<x[i+1]:
                return False
        return True
        
        
A=int(input('Digite a quantidade de elementos:'))
a=[]
for i in range(0,A,1):
    d=int(input('Digite o valor:'))
    a.append(d)
    
if pico(a):
    print('S')
else:
    print('N')
        
        


    
    









