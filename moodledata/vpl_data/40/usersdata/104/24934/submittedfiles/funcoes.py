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
    z=2
    for i in range(1,m+1,1):
        if cont==0:
            pi=pi+(4/(fatorial(z+2)/fatorial(z-1)))
            cont=1
        else:
            pi=pi-(4/(fatorial(z+2)/fatorial(z-1)))
    return pi        
def calcula_co_seno(z,epsilon):
    i=2
    cos_z=1
    cont=0
    y=(x**i)/(fatorial(i))
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

print calcula_pi(1)
