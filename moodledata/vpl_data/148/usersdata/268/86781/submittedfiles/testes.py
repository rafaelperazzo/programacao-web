# -*- coding: utf-8 -*-

def impar(x):
    if x%2==1:
        return(True)
    else:
        return(False)
for i in range(1000,10000,1):
    cont=0
    soma=0
    if impar(i)==True:
         while(i>0):
             if impar(cont)==False:
                 soma= soma -i%10
                 
             if impar(cont)==True:
                 soma=soma + i%10
                 
             if soma<0:
                 print(i)
             i=i//10
             