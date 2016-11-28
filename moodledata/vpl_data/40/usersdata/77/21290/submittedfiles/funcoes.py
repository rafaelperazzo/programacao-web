#ARQUIVO COM SUAS FUNCOES

def calcula_pi(m):
    soma=0
    i=1
    j=e
    while i<=n:
        if 1<=m and m<=2000:
            if i%2==0:
                soma=soma-(4/(j*(j+1)*(j+2)))
            else:
                soma=soma+(4/(j*(j+1)*(j+2)))
        i=i+1
        j=j+2
    pi=3+soma
    return pi

def calcula_valor_absoluto(x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
def fatorial(n):
    fatorial=1
    i=1
    while i<=n:
        fatorial=fatorial*i
        
        i=i+1
    return fatorial

def calcula_co_seno(z,e):
    i=1
    j=2
    soma=0
    termo=((z**j)fatorial(j))
    while termo>e:
        if i%2!=0:
            soma=soma-termo
        else:
            soma=soma+termo
        
        i=i+1
        j=j+2
        termo=((z**j)fatorial(j))
        
    cos=1+soma
    return cos
    
def calcula_razão_aurea(m,e):
    operacao=calcula_co_seno((calcula_pi(m)/5.0,e)
    razao_aurea=2*operacao
    
    return razao_aurea
        