# -*- coding: utf-8 -*-
def soma(n):
    for a in range (1,n+1,1):
        for b in range (1,n+1,1):
            for c in range (1,n+1,1):
                if a+b+c==n:
                    if (a*a)+(b*b)==(c*c):
                        return (a,b,c)
                    else:
                        return ('N')
    else:
        return ('N')
n=int(input('Digite n:'))

print(soma(n))