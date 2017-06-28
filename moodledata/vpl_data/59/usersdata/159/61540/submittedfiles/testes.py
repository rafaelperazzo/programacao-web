# -*- coding: utf-8 -*-
def soma(n):
    for a in range (1,n+1,1):
        for b in range (1,n+1,1):
            for c in range (1,n+1,1):
                if a+b+c==n:
                    if (a**2)+(b**2)==(c**2):
                        return (a,b,c)
                    else:
                        return ('N')
                else:
                    return ('N')
n=int(input('Digite n:'))

print(soma(n))