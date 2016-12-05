def fatorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    return f
def calcula_valor_absoluto(x):
    if x>=0:
        return (x)
    else:
        return (-x)
def calcula_pi(m):
    pi=3
    cont=0
    z=4
    w=(fatorial(z)/fatorial(z-3))
    for i in range(1,m+1,1):
        if cont==0:
            pi=pi+(4/w)
            cont=1
        else:
            pi=pi-(4/w)
            cont=0
        z=z+2
    return pi        
def calcula_co_seno(z,epsilon):
    i=2
    cos_z=1
    cont=0
    y=(z**i)/(fatorial(i))
    mod=calcula_valor_absoluto(y)
    while mod>=epsilon:
        if cont==0:
            cos_z=(cos_z)-y
            cont=1
        else:
            cos_z=(cos_z)+y
            cont=0
        i=i+2
        mod=calcula_valor_absoluto(y)
    return cos_z
def calcula_razao_aurea(m,epsilon):
    pi=calcula_pi(m)
    phi=2*((calcula_co_seno(pi,epsilon))/5)
    return phi
