# -*- coding: utf-8 -*-
m = int(input('Digite a quantidade de termos n: '))
n = []

def maiordegrau(m,n):
    for i in range(1,n+1,1):
        h = n - (n-1)
        if h<0:
            h = h*(-1)
    return(h)
print(maiordegrau(5,4))    
        

