# -*- coding: utf-8 -*-
def pi(m):
    soma=3
    x=2
    y=3
    z=4
    for termo in range(1,m-1,1):
        if termo%2==0:
            soma=soma-(4/(x*y*z))
        else:
            soma=soma+(4/(x*y*z))
        x=x+2
        y+y+2
        z=z+2
    return (soma)
m=int(input('m: '))
print(pi(m))