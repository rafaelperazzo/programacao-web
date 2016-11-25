#ARQUIVO COM SUAS FUNCOES

def calcula_pi (m):
    i=1
    soma=0
    a=2
    while i<=m:
        if 1<=m and m<=2000:
            if i%2==0:
                soma=soma-(4/(a*(a+1)*(a+2)))
            else:
                soma=soma+(4/(a*(a+1)*(a+2)))
        i=i+1
        a=a+2
    pi=3+soma
    return pi

def calcula_valor_absoluto (x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x

def fatorial (x):
    fatorial=1
    i=1
    while i<=x:
        fatorial=fatorial*i
        i=i+1
    return fatorial

def calcula_co_sen (x,y):
    i=1
    b=2
    soma=0
    termo=((x**b)/fatorial(b)
    while termo > y:
        termo=((z**b)/fatorial(b))
        if i%2!=0:
            soma=soma-termo
        else:
            soma=soma+termo
        i=i+1
        b=b+2
    cos=1+soma
    return cos

def calcula_razao_aurea (x,y):
    operacao=calcula_co_sen((calcula_pi(x))/5,y)
    razao_aurea=2*operacao
    return razao_aurea