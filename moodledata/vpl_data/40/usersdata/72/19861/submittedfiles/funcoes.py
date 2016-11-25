#ARQUIVO COM SUAS FUNCOES
#CALCULAR O VALOR DE PI

def calcula_pi (m):
    i=1
    soma=0
    a=2
    while i<=m:
        if 1<=m and m<=2000:
            if i%==0:
                soma=soma-(4/(a*(a+1)*(a+2)))
            else:
                soma=soma+(4/a*(a+1)*(a+2)))
        i=i+1
        a=a+2
    pi=3+soma
    return pi
    
#CALCULAR O VALOR ABSOLUTO

def calcula_valor_absoluto (x):
    if x<0:
        x=x*(-1)
        return x
    else:
        return x
        
#CALCULAR O FATORIAL 

def fatorial (n):
    fatorial=1
    i=1
    while i<=n:
        fatorial=fatorial*i
        i=i+1
    return fatorial
    
#CALCULAR O VALOR DO COSSENO

def calcula_co_sen (z,e):
    