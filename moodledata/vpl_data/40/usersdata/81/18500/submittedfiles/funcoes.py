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
    for i in range (1,m+1,1):
        if i%2==0:
            soma_pi=soma_pi+(4/(j*(j+1)*(j+2)))
        else:
            soma_pi=soma_pi-(4/(j*(j+1)*(j+2)))
        j=j+2    
        pi=3+soma_pi
return pi

def calcula_co_seno(z,epsilon):
    soma_cos=0
    j=2

    while i<m and soma_cosseno==e:
        if i%2!=0:
            soma_cos=soma_cos+(((pi/5)**j)/fatorial(j))
        else:
            soma_cos=soma_cos-(((pi/5)**j)/fatorial(j))
        j=j+2
        i=i+1
    
        cosseno=1-soma_cos
return cosseno
    
def calcula_razao_aurea(m,epsilon):
    razao= 2*calcula_cos_sen(z,epsilon)
    return razao