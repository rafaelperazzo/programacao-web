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
    cont=0
    pi=3
    for i in range(2,((2*m)+1),1):
        if cont=0:
            pi=pi+(4/(fatorial(i+2)/fatorial
def calcula_co_seno(z,epsilon):
    i=2
    cos_z=1
    cont=0
    y=(x**i)/(fatorial(i))
    mod=calcula_valor_absoluto(y)
    while mod>=epsilon:
        if cont=0:
            cos_z=(cos_z)-y
            cont=1:
        else:
            cos_z=(cos_z)+y
            cont=0
        i=i+2
    return cos_z