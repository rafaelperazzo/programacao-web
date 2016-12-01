#ARQUIVO COM SUAS FUNCOES

def modulo(m):
    if m<0:
        m=m*(-1)
    return m
    
def fatorial(f):
    fator=1
    for i in range(2,f+1,1):
        fator=fator*i
    return fator

def pi(p):
    soma=0
    j=2
    for i in range(0,p,1):
        if i%2==0:
            soma=soma+(4/(j*(j+1)*(j+2)))
        else:
            soma=soma-(4/(j*(j+1)*(j+2)))
        j=j+2
    PI=3+soma
    return PI
    
def cosseno(c,e):
    soma=0
    i=1
    j=2
    a=(z**j)/fatorial(j)
    while a>e:
        a=(z**j)/fatorial(j)
        if i%2!=0:
            soma=soma+a
        else:
            soma=soma-a
        j=j+2
        i=i+1
    cos=1-soma
    return cos
    
def RA(r,e):
    Pi=pi(r)
    Cos=cosseno(Pi/5,e)
    razaoA=2*Cos
    return razaoA
    
    