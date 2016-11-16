
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
    somapi=0
    j=2
    for i in range (1,m+1,1):
        if i%2==0:
            somapi=somapi-(4/(j*(j+1)*(j+2)))
        else:
            somapi=somapi+(4/(j*(j+1)*(j+2)))
        j=j+2    
    p=somapi+3
    return p