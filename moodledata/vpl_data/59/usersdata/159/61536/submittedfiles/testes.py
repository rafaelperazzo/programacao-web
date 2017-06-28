# -*- coding: utf-8 -*-
def soma(n):
    lista=[]
    x=0
    for a in range (1,n+1,1):
        for b in range (1,n+1,1):
            for c in range (1,n+1,1):
                if a+b+c==n:
                    if a**2+b**2==c:
                        return (a,b,c)
                    else:
                        return ('N')
n=int(input('Digite n:'))

print(soma(n))