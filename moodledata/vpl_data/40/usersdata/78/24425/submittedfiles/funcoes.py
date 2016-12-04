#ARQUIVO COM SUAS FUNCOES

def absoluto(m):
    if m<0:
        m=m*(-1)
        return m
    else:
        return m
        
def fatorial(m):
    fat=1
    for i in range(2,m+1,1):
        fat=fat*(i)
    return fat

def pi(m):
    soma=0
    j=2
    i=0
    while i<m:
        if i%2==0:
            soma=soma-(4/(j*(j+1)*(j+2)))
        else:
            soma=soma+(4/(j*(j+1)*(j+2)))
        i=i+1
        j=j+2
    pi=3+soma
    return pi
    
def cosseno(z,e):
    soma=0
    i=1
    a=2
    c=(z**a)/fatorial(a)
    while c>e:
        if i%2!=0:
            soma=soma+c
        else:
            soma=soma-c
        i=i+1
        a=a+2
    cosseno=1-soma
    return cosseno
    
def razaoaurea(m,e):
    pi=pi(m)
    cosseno=cosseno(pi/5,e)
    razaoaurea=2*cosseno
    return razaoaurea