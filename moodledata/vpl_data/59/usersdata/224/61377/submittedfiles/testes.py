# -*- coding: utf-8 -*-
def pi(m):
    soma=3
    x=2
    y=3
    z=4
    for termo in range(1,m+1,1):
        if termo%2==0:
            soma=soma-(4/(x*y*z))
        else:
            soma=soma+(4/(x*y*z))
        x=x+2
        y=y+2
        z=z+2
    return ('%.15f'%(soma))
def cosseno(z,epsilon):
    soma=1
    i=2
    fatorial=2
    v=1
    termo=1
    while termo>=epsilon:
        termo=(z**i)/fatorial
        if v%2==0:
            soma=soma+termo
        else:
            soma=soma-termo
        i=i+2
        fatorial=fatorial*(i-1)*i
        v=v+1
    return (soma)
def razaoaurea(m,epsilon):
    razao=2*(cosseno(pi(m)/5,epsilon))
    return('%.15f'%(razao))

m=int(input('m:'))
epsilon=float(input('epsilon:'))
print(pi(m))
print(razaoaurea(m,epsilon))