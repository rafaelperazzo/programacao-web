def fatorial(n):
    n_fat=1
    for i in range(1,n+1,1):
        n_fat*=n
        return n_fat

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
    return x

def pi(m):    
    soma_pi=0
    j=2
    for i in range (0,m,1):
        if i%2==0:
            soma_pi=soma_pi+(4/(j*(j+1)*(j+2)))
        else:
            soma_pi=soma_pi-(4/(j*(j+1)*(j+2)))
        j=j+2    
    pi=3+soma_pi
    return pi
